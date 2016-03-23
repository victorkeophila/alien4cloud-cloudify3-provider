package alien4cloud.paas.cloudify3.service;

import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.locks.ReentrantReadWriteLock;

import javax.annotation.PostConstruct;
import javax.annotation.Resource;

import lombok.extern.slf4j.Slf4j;

import org.apache.commons.collections4.MapUtils;
import org.apache.commons.lang3.exception.ExceptionUtils;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Component;
import org.springframework.web.client.HttpClientErrorException;

import alien4cloud.model.topology.NodeTemplate;
import alien4cloud.paas.IPaaSCallback;
import alien4cloud.paas.cloudify3.configuration.CloudConfiguration;
import alien4cloud.paas.cloudify3.configuration.CloudConfigurationHolder;
import alien4cloud.paas.cloudify3.configuration.ICloudConfigurationChangeListener;
import alien4cloud.paas.cloudify3.configuration.MappingConfigurationHolder;
import alien4cloud.paas.cloudify3.model.AbstractCloudifyModel;
import alien4cloud.paas.cloudify3.model.Deployment;
import alien4cloud.paas.cloudify3.model.Execution;
import alien4cloud.paas.cloudify3.model.ExecutionStatus;
import alien4cloud.paas.cloudify3.model.Node;
import alien4cloud.paas.cloudify3.model.NodeInstance;
import alien4cloud.paas.cloudify3.model.NodeInstanceStatus;
import alien4cloud.paas.cloudify3.model.Workflow;
import alien4cloud.paas.cloudify3.restclient.DeploymentClient;
import alien4cloud.paas.cloudify3.restclient.ExecutionClient;
import alien4cloud.paas.cloudify3.restclient.NodeClient;
import alien4cloud.paas.cloudify3.restclient.NodeInstanceClient;
import alien4cloud.paas.cloudify3.util.DateUtil;
import alien4cloud.paas.model.DeploymentStatus;
import alien4cloud.paas.model.InstanceInformation;
import alien4cloud.paas.model.InstanceStatus;
import alien4cloud.paas.model.PaaSTopologyDeploymentContext;
import alien4cloud.utils.MapUtil;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.google.common.collect.Maps;
import com.google.common.collect.Sets;
import com.google.common.util.concurrent.FutureCallback;
import com.google.common.util.concurrent.Futures;
import com.google.common.util.concurrent.ListenableFuture;
import com.google.common.util.concurrent.ListeningScheduledExecutorService;

/**
 * Handle all deployment status request
 */
@Component("cloudify-status-service")
@Slf4j
public class StatusService {

    private Map<String, DeploymentStatus> statusCache = Maps.newHashMap();

    private ReentrantReadWriteLock cacheLock = new ReentrantReadWriteLock();

    @Resource
    private EventService eventService;

    @Resource
    private ExecutionClient executionDAO;

    @Resource
    private NodeInstanceClient nodeInstanceDAO;

    @Resource
    private NodeClient nodeDAO;

    @Resource
    private DeploymentClient deploymentDAO;

    @Resource
    private CloudConfigurationHolder cloudConfigurationHolder;

    @Resource
    private MappingConfigurationHolder mappingConfigurationHolder;

    @Resource
    private RuntimePropertiesService runtimePropertiesService;

    @Resource
    private ListeningScheduledExecutorService scheduler;

    @PostConstruct
    public void postConstruct() {
        cloudConfigurationHolder.registerListener(new ICloudConfigurationChangeListener() {
            @Override
            public void onConfigurationChange(CloudConfiguration newConfiguration) throws Exception {
                init();
            }
        });
    }

    private void scheduleRefreshStatus(final String deploymentPaaSId, final DeploymentStatus currentStatus) {
        long scheduleTime;
        switch (currentStatus) {
        case DEPLOYMENT_IN_PROGRESS:
        case UNDEPLOYMENT_IN_PROGRESS:
            // Poll more aggressively if deployment in progress or undeployment in progress
            scheduleTime = 5;
            break;
        default:
            scheduleTime = 60;
            break;
        }
        scheduler.schedule(new Runnable() {
            @Override
            public void run() {
                // Try to refresh the status
                log.info("Running refresh state for {} with current state {}", deploymentPaaSId, currentStatus);
                try {
                    cacheLock.readLock().lock();
                    // It means someone cleaned entry before the scheduled task run
                    if (!statusCache.containsKey(deploymentPaaSId)) {
                        return;
                    }
                } finally {
                    cacheLock.readLock().unlock();
                }
                DeploymentStatus newStatus = doGetStatus(deploymentPaaSId);
                if (newStatus != null) {
                    registerDeploymentStatus(deploymentPaaSId, newStatus);
                }
                // new status is null it means that it is intermediary status
                // Will just ignore and re-schedule a polling
                scheduleRefreshStatus(deploymentPaaSId, currentStatus);
            }
        }, scheduleTime, TimeUnit.SECONDS);
    }

    private void init() throws Exception {
        Deployment[] deployments = deploymentDAO.list();
        for (final Deployment deployment : deployments) {
            DeploymentStatus deploymentStatus = doGetStatus(deployment);
            if (deploymentStatus != null && !DeploymentStatus.UNDEPLOYED.equals(deploymentStatus)) {
                registerDeploymentStatus(deployment.getId(), deploymentStatus);
            }
        }
    }

    private DeploymentStatus doGetStatus(Deployment deployment) {
        Execution[] executions;
        try {
            executions = executionDAO.list(deployment.getId(), false);
        } catch (Exception exception) {
            return DeploymentStatus.UNKNOWN;
        }
        return doGetStatus(deployment.getId(), executions);
    }

    private DeploymentStatus doGetStatus(String deploymentPaaSId) {
        try {
            Deployment deployment = deploymentDAO.read(deploymentPaaSId);
            if (deployment == null) {
                return DeploymentStatus.UNDEPLOYED;
            } else {
                return doGetStatus(deployment);
            }
        } catch (Exception e) {
            Throwable rootCause = ExceptionUtils.getRootCause(e);
            if (rootCause instanceof HttpClientErrorException) {
                if (((HttpClientErrorException) rootCause).getStatusCode().equals(HttpStatus.NOT_FOUND)) {
                    // Only return undeployed for an application if we received a 404 which means it was deleted
                    return DeploymentStatus.UNDEPLOYED;
                }
            }
            return DeploymentStatus.UNKNOWN;
        }
    }

    private DeploymentStatus doGetStatus(String deploymentPaaSId, Execution[] executions) {
        Execution lastExecution = null;
        // Get the last install or uninstall execution, to check for status
        for (Execution execution : executions) {
            if (log.isDebugEnabled()) {
                log.debug("Deployment {} has execution {} created at {} for workflow {} in status {}", deploymentPaaSId, execution.getId(),
                        execution.getCreatedAt(), execution.getWorkflowId(), execution.getStatus());
            }
            Set<String> relevantExecutionsForStatus = Sets.newHashSet(Workflow.INSTALL, Workflow.DELETE_DEPLOYMENT_ENVIRONMENT,
                    Workflow.CREATE_DEPLOYMENT_ENVIRONMENT, Workflow.UNINSTALL);
            // Only consider install/uninstall workflow to check for deployment status
            if (relevantExecutionsForStatus.contains(execution.getWorkflowId())) {
                if (lastExecution == null) {
                    lastExecution = execution;
                } else if (DateUtil.compare(execution.getCreatedAt(), lastExecution.getCreatedAt()) > 0) {
                    lastExecution = execution;
                }
            }
        }
        // No install and uninstall yet it must be deployment in progress
        if (lastExecution == null) {
            return DeploymentStatus.DEPLOYMENT_IN_PROGRESS;
        } else {
            // Only consider changing state when an execution has been finished or in failure
            // Execution in cancel or starting will return null to not impact on the application state as they are intermediary state
            switch (lastExecution.getWorkflowId()) {
            case Workflow.CREATE_DEPLOYMENT_ENVIRONMENT:
                if (ExecutionStatus.isTerminatedSuccessfully(lastExecution.getStatus())) {
                    return DeploymentStatus.DEPLOYMENT_IN_PROGRESS;
                } else if (ExecutionStatus.isTerminatedWithFailure(lastExecution.getStatus())) {
                    return DeploymentStatus.FAILURE;
                } else {
                    return null;
                }
            case Workflow.INSTALL:
                if (ExecutionStatus.isTerminatedSuccessfully(lastExecution.getStatus())) {
                    return DeploymentStatus.DEPLOYED;
                } else if (ExecutionStatus.isTerminatedWithFailure(lastExecution.getStatus())) {
                    return DeploymentStatus.FAILURE;
                } else {
                    return null;
                }
            case Workflow.UNINSTALL:
                if (ExecutionStatus.isTerminatedSuccessfully(lastExecution.getStatus())) {
                    return DeploymentStatus.UNDEPLOYMENT_IN_PROGRESS;
                } else if (ExecutionStatus.isTerminatedWithFailure(lastExecution.getStatus())) {
                    return DeploymentStatus.FAILURE;
                } else {
                    return null;
                }
            case Workflow.DELETE_DEPLOYMENT_ENVIRONMENT:
                if (ExecutionStatus.isTerminatedSuccessfully(lastExecution.getStatus())) {
                    return DeploymentStatus.UNDEPLOYED;
                } else if (ExecutionStatus.isTerminatedWithFailure(lastExecution.getStatus())) {
                    return DeploymentStatus.FAILURE;
                } else {
                    return null;
                }
            default:
                return DeploymentStatus.UNKNOWN;
            }
        }
    }

    public DeploymentStatus getStatus(String deploymentPaaSId) {
        try {
            cacheLock.readLock().lock();
            if (!statusCache.containsKey(deploymentPaaSId)) {
                return DeploymentStatus.UNDEPLOYED;
            } else {
                return statusCache.get(deploymentPaaSId);
            }
        } finally {
            cacheLock.readLock().unlock();
        }
    }

    public void getStatus(String deploymentPaaSId, IPaaSCallback<DeploymentStatus> callback) {
        callback.onSuccess(getStatus(deploymentPaaSId));
    }

    public void getInstancesInformation(final PaaSTopologyDeploymentContext deploymentContext,
            final IPaaSCallback<Map<String, Map<String, InstanceInformation>>> callback) {
        try {
            cacheLock.readLock().lock();
            if (!statusCache.containsKey(deploymentContext.getDeploymentPaaSId())) {
                callback.onSuccess(Maps.<String, Map<String, InstanceInformation>> newHashMap());
                return;
            }
        } finally {
            cacheLock.readLock().unlock();
        }
        ListenableFuture<NodeInstance[]> instancesFuture = nodeInstanceDAO.asyncList(deploymentContext.getDeploymentPaaSId());
        ListenableFuture<Node[]> nodesFuture = nodeDAO.asyncList(deploymentContext.getDeploymentPaaSId(), null);
        ListenableFuture<List<AbstractCloudifyModel[]>> combinedFutures = Futures.allAsList(instancesFuture, nodesFuture);
        Futures.addCallback(combinedFutures, new FutureCallback<List<AbstractCloudifyModel[]>>() {
            @Override
            public void onSuccess(List<AbstractCloudifyModel[]> nodeAndNodeInstances) {
                NodeInstance[] instances = (NodeInstance[]) nodeAndNodeInstances.get(0);
                Node[] nodes = (Node[]) nodeAndNodeInstances.get(1);
                Map<String, Node> nodeMap = Maps.newHashMap();
                for (Node node : nodes) {
                    nodeMap.put(node.getId(), node);
                }

                Map<String, NodeInstance> nodeInstanceMap = Maps.newHashMap();
                for (NodeInstance instance : instances) {
                    nodeInstanceMap.put(instance.getId(), instance);
                }

                Map<String, Map<String, InstanceInformation>> information = Maps.newHashMap();
                for (NodeInstance instance : instances) {
                    NodeTemplate nodeTemplate = deploymentContext.getDeploymentTopology().getNodeTemplates().get(instance.getNodeId());
                    if (nodeTemplate == null) {
                        // Sometimes we have generated instance that do not exist in alien topology
                        continue;
                    }
                    Map<String, InstanceInformation> nodeInformation = information.get(instance.getNodeId());
                    if (nodeInformation == null) {
                        nodeInformation = Maps.newHashMap();
                        information.put(instance.getNodeId(), nodeInformation);
                    }
                    String instanceId = instance.getId();
                    InstanceInformation instanceInformation = new InstanceInformation();
                    instanceInformation.setState(instance.getState());
                    InstanceStatus instanceStatus = NodeInstanceStatus.getInstanceStatusFromState(instance.getState());
                    if (instanceStatus == null) {
                        continue;
                    } else {
                        instanceInformation.setInstanceStatus(instanceStatus);
                    }
                    Map<String, String> runtimeProperties = null;
                    try {
                        runtimeProperties = MapUtil.toString(instance.getRuntimeProperties());
                    } catch (JsonProcessingException e) {
                        log.error("Unable to stringify runtime properties", e);
                    }
                    instanceInformation.setRuntimeProperties(runtimeProperties);
                    Node node = nodeMap.get(instance.getNodeId());
                    if (node != null && runtimeProperties != null) {
                        instanceInformation.setAttributes(runtimePropertiesService.getAttributes(node, instance, nodeMap, nodeInstanceMap));
                    }
                    nodeInformation.put(instanceId, instanceInformation);
                }
                String floatingIpPrefix = mappingConfigurationHolder.getMappingConfiguration().getGeneratedNodePrefix() + "_floating_ip_";
                for (NodeInstance instance : instances) {
                    if (instance.getId().startsWith(floatingIpPrefix)) {
                        // It's a floating ip then must fill the compute with public ip address
                        String computeNodeId = instance.getNodeId().substring(floatingIpPrefix.length());
                        Map<String, InstanceInformation> computeNodeInformation = information.get(computeNodeId);
                        if (MapUtils.isNotEmpty(computeNodeInformation)) {
                            InstanceInformation firstComputeInstanceFound = computeNodeInformation.values().iterator().next();
                            firstComputeInstanceFound.getAttributes().put("public_ip_address",
                                    String.valueOf(instance.getRuntimeProperties().get("floating_ip_address")));
                        }
                    }
                }
                // [[ Scaling issue workarround
                // Code for scaling workaround : here we are looking for the _a4c_substitute_for property of the node
                // if it contains something, this means that this node is substituting others
                // we generate 'fake' instances for these ghosts nodes
                for (Entry<String, Node> nodeEntry : nodeMap.entrySet()) {
                    List substitutePropertyAsList = ScalableComputeReplacementService.getSubstituteForPropertyAsList(nodeEntry.getValue());
                    if (substitutePropertyAsList != null) {
                        Map<String, InstanceInformation> instancesInfo = information.get(nodeEntry.getKey());
                        for (Object substitutePropertyItem : substitutePropertyAsList) {
                            String substitutedNodeId = substitutePropertyItem.toString();
                            Map<String, InstanceInformation> nodeInformation = Maps.newHashMap();
                            information.put(substitutedNodeId, nodeInformation);
                            for (Entry<String, InstanceInformation> instanceEntry : instancesInfo.entrySet()) {
                                InstanceInformation ii = new InstanceInformation();
                                ii.setState(instanceEntry.getValue().getState());
                                ii.setInstanceStatus(instanceEntry.getValue().getInstanceStatus());
                                // TODO map runtime properties ?
                                nodeInformation.put(instanceEntry.getKey(), ii);
                            }
                        }
                    }
                }
                // Scaling issue workarround ]]
                callback.onSuccess(information);
            }

            @Override
            public void onFailure(Throwable t) {
                if (log.isDebugEnabled()) {
                    log.debug("Problem retrieving instance information for deployment <" + deploymentContext.getDeploymentPaaSId() + "> ");
                }
                callback.onSuccess(Maps.<String, Map<String, InstanceInformation>> newHashMap());
            }
        });
    }

    public void registerDeploymentStatus(String deploymentPaaSId, DeploymentStatus newDeploymentStatus) {
        try {
            cacheLock.writeLock().lock();
            if (DeploymentStatus.UNDEPLOYED.equals(newDeploymentStatus)) {
                if (statusCache.containsKey(deploymentPaaSId)) {
                    statusCache.remove(deploymentPaaSId);
                    eventService.registerDeploymentEvent(deploymentPaaSId, DeploymentStatus.UNDEPLOYED);
                }
            } else {
                DeploymentStatus deploymentStatus = statusCache.get(deploymentPaaSId);
                if (!newDeploymentStatus.equals(deploymentStatus)) {
                    // Deployment status has changed
                    statusCache.put(deploymentPaaSId, newDeploymentStatus);
                    eventService.registerDeploymentEvent(deploymentPaaSId, newDeploymentStatus);
                }
                // Schedule a refresh only if it's a new entry
                if (deploymentStatus == null) {
                    scheduleRefreshStatus(deploymentPaaSId, newDeploymentStatus);
                }
            }
        } finally {
            cacheLock.writeLock().unlock();
        }
    }
}
