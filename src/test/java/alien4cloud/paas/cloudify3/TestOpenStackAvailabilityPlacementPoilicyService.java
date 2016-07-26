package alien4cloud.paas.cloudify3;

import static org.junit.Assert.assertEquals;

import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.Map;
import java.util.Set;

import javax.annotation.PostConstruct;
import javax.annotation.Resource;
import javax.inject.Inject;
import javax.validation.constraints.AssertTrue;

import alien4cloud.model.orchestrators.locations.LocationResourceTemplate;
import alien4cloud.model.topology.AbstractPolicy;
import alien4cloud.model.topology.HaPolicy;
import alien4cloud.model.topology.NodeGroup;
import alien4cloud.paas.cloudify3.service.OpenStackAvailabilityZonePlacementPolicyService;
import alien4cloud.paas.model.PaaSNodeTemplate;
import alien4cloud.topology.TopologyUtils;
import com.google.common.collect.Lists;
import com.google.common.collect.Sets;
import lombok.Getter;
import lombok.extern.slf4j.Slf4j;

import org.elasticsearch.common.collect.Maps;
import org.junit.Before;
import org.junit.Ignore;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.context.ApplicationContext;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import alien4cloud.component.repository.ArtifactLocalRepository;
import alien4cloud.component.repository.ArtifactRepositoryConstants;
import alien4cloud.model.components.DeploymentArtifact;
import alien4cloud.model.components.FunctionPropertyValue;
import alien4cloud.model.components.IValue;
import alien4cloud.model.components.ScalarPropertyValue;
import alien4cloud.orchestrators.plugin.ILocationConfiguratorPlugin;
import alien4cloud.paas.cloudify3.location.AmazonLocationConfigurator;
import alien4cloud.paas.cloudify3.location.ByonLocationConfigurator;
import alien4cloud.paas.cloudify3.location.OpenstackLocationConfigurator;
import alien4cloud.paas.cloudify3.service.PropertyEvaluatorService;
import alien4cloud.paas.cloudify3.util.ApplicationUtil;
import alien4cloud.paas.cloudify3.util.CSARUtil;
import alien4cloud.paas.cloudify3.util.DeploymentLauncher;
import alien4cloud.paas.model.PaaSTopologyDeploymentContext;

import com.google.common.io.Closeables;

@Slf4j
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration("classpath:test-context.xml")
public class TestOpenStackAvailabilityPlacementPoilicyService extends AbstractTest {

    private static final String  GROUP_NAME = "Alien-HA";
    @Inject
    private ApplicationContext applicationContext;

    @Resource
    private DeploymentLauncher deploymentLauncher;

    @Resource
    private ApplicationUtil applicationUtil;

    @Resource
    private PropertyEvaluatorService propertyEvaluatorService;

    @Getter
    private Map<String, ILocationConfiguratorPlugin> locationsConfigurators = Maps.newHashMap();

    @Inject
    private OpenStackAvailabilityZonePlacementPolicyService osAzPPolicyService;

    @Resource
    private CSARUtil csarUtil;

    private NodeGroup nodeGroup = null;

    @Override
    public void before() throws Exception {
        super.before();
    }

    @Test
    public void testProcessTopology() {
        StackTraceElement[] stackTraceElements = Thread.currentThread().getStackTrace();
        PaaSTopologyDeploymentContext context = deploymentLauncher.buildPaaSDeploymentContext(stackTraceElements[2].getMethodName(), SINGLE_COMPUTE_TOPOLOGY, "openstack");
        String nodeName = context.getPaaSTopology().getAllNodes().keySet().toArray(new String[1])[0];
        context.getDeploymentTopology().setGroups(Maps.<String, NodeGroup>newHashMap());
        context.getDeploymentTopology().getGroups().put(nodeGroup.getName(), nodeGroup);
        context.getPaaSTopology().getAllNodes().get(nodeName).getTemplate().setGroups(Sets.<String>newHashSet());
        context.getPaaSTopology().getAllNodes().get(nodeName).getTemplate().getGroups().add(nodeGroup.getName());



        Map<String, PaaSNodeTemplate> allNodes = Maps.<String, PaaSNodeTemplate> newHashMap();
        List<LocationResourceTemplate> availabilityZones = Lists.<LocationResourceTemplate> newArrayList();
        LocationResourceTemplate locationResourceTemplate = new LocationResourceTemplate();
//        locationResourceTemplate.setTemplate();

        //  availabilityZone.getTemplate().getProperties().get("id")).getValue()

        Set<String> members;

//        osAzPPolicyService.setAZForAllNodes("fake-id", allNodes, availabilityZones, GROUP_NAME, members);
    }
}
