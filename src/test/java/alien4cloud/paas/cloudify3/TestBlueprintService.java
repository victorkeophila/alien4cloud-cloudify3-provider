package alien4cloud.paas.cloudify3;

import static org.junit.Assert.assertEquals;

import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.Set;

import javax.annotation.Resource;

import lombok.SneakyThrows;
import lombok.extern.slf4j.Slf4j;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import alien4cloud.component.repository.ArtifactLocalRepository;
import alien4cloud.component.repository.ArtifactRepositoryConstants;
import alien4cloud.model.components.DeploymentArtifact;
import alien4cloud.model.components.FunctionPropertyValue;
import alien4cloud.model.components.IValue;
import alien4cloud.model.components.ScalarPropertyValue;
import alien4cloud.paas.cloudify3.service.BlueprintService;
import alien4cloud.paas.cloudify3.service.CloudifyDeploymentBuilderService;
import alien4cloud.paas.cloudify3.service.PropertyEvaluatorService;
import alien4cloud.paas.cloudify3.service.ScalableComputeReplacementService;
import alien4cloud.paas.cloudify3.util.ApplicationUtil;
import alien4cloud.paas.cloudify3.util.DeploymentLauncher;
import alien4cloud.paas.cloudify3.util.FileTestUtil;
import alien4cloud.paas.model.PaaSTopologyDeploymentContext;
import alien4cloud.utils.FileUtil;

import com.google.common.collect.Sets;
import com.google.common.io.Closeables;

@Slf4j
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration("classpath:test-context.xml")
public class TestBlueprintService extends AbstractTest {

    @Resource
    private BlueprintService blueprintService;

    @Resource
    private CloudifyDeploymentBuilderService cloudifyDeploymentBuilderService;

    @Resource
    private DeploymentLauncher deploymentLauncher;

    @Resource
    private ApplicationUtil applicationUtil;

    @Resource
    private ArtifactLocalRepository artifactRepository;

    @Resource
    private ScalableComputeReplacementService scalableComputeReplacementService;

    @Resource
    private PropertyEvaluatorService propertyEvaluatorService;

    /**
     * Set true to this boolean when the blueprint has changed and you want to re-register
     */
    private boolean record = false;

    /**
     * Set true to this boolean so the blueprint will be uploaded to the manager to verify
     */
    private boolean verifyBlueprintUpload = false;

    private static final Set<String> LOCATIONS = Sets.newHashSet();

    static {
        LOCATIONS.add("openstack");
        LOCATIONS.add("amazon");
        LOCATIONS.add("byon");
    }

    @Override
    @Before
    public void before() throws Exception {
        Assert.assertTrue("This test only works on Java version 1.7", System.getProperty("java.version").startsWith("1.7"));
        super.before();
    }

    private interface DeploymentContextVisitor {
        void visitDeploymentContext(PaaSTopologyDeploymentContext context) throws Exception;
    }

    @SneakyThrows
    private void testGeneratedBlueprintFile(String topology) {
        StackTraceElement[] stackTraceElements = Thread.currentThread().getStackTrace();
        for (String location : LOCATIONS) {
            testGeneratedBlueprintFile(topology, location, topology, stackTraceElements[2].getMethodName(), null);
        }
    }

    @SneakyThrows
    private Path testGeneratedBlueprintFile(String topology, String locationName, String outputFile, String testName, DeploymentContextVisitor contextVisitor) {
        if (!applicationUtil.isTopologyExistForLocation(topology, locationName)) {
            log.warn("Topology {} do not exist for location {}", topology, locationName);
            return null;
        }
        String recordedDirectory = "src/test/resources/outputs/blueprints/" + locationName + "/" + outputFile;
        PaaSTopologyDeploymentContext context = deploymentLauncher.buildPaaSDeploymentContext(testName, topology, locationName);
        if (contextVisitor != null) {
            contextVisitor.visitDeploymentContext(context);
        }
        propertyEvaluatorService.processGetPropertyFunction(context);
        context = scalableComputeReplacementService.transformTopology(context);
        Path generated = blueprintService.generateBlueprint(cloudifyDeploymentBuilderService.buildCloudifyDeployment(context));
        Path generatedDirectory = generated.getParent();
        if (record) {
            FileUtil.delete(Paths.get(recordedDirectory));
            FileUtil.copy(generatedDirectory, Paths.get(recordedDirectory), StandardCopyOption.REPLACE_EXISTING);
            if (verifyBlueprintUpload) {
                deploymentLauncher.verifyBlueprintUpload(topology, generated.toString());
            }
        } else {
            FileTestUtil.assertFilesAreSame(Paths.get(recordedDirectory), generatedDirectory, ".+.zip", ".+/cloudify-openstack-plugin/.+", ".+/monitor/.+");
        }
        return generated;
    }

    @Test
    public void testGenerateSingleCompute() {
        testGeneratedBlueprintFile(SINGLE_COMPUTE_TOPOLOGY);
    }

    @Test
    public void testGenerateScalableCompute() {
        String oldImport = cloudConfigurationHolder.getConfiguration().getLocations().getOpenstack().getImports().get(1);
        cloudConfigurationHolder.getConfiguration().getLocations().getOpenstack().getImports().set(1, "openstack-plugin.yaml");
        testGeneratedBlueprintFile(SCALABLE_COMPUTE_TOPOLOGY);
        cloudConfigurationHolder.getConfiguration().getLocations().getOpenstack().getImports().set(1, oldImport);
    }

    @Test
    public void testGenerateSingleWindowsCompute() {
        testGeneratedBlueprintFile(SINGLE_WINDOWS_COMPUTE_TOPOLOGY);
    }

    @Test
    public void testGenerateNetwork() {
        testGeneratedBlueprintFile(NETWORK_TOPOLOGY);
    }

    @Test
    public void testGenerateLamp() {
        testGeneratedBlueprintFile(LAMP_TOPOLOGY);
    }

    @Test
    public void testGenerateBlockStorage() {
        testGeneratedBlueprintFile(STORAGE_TOPOLOGY);
    }

    @Test
    public void testGenerateTomcat() {
        testGeneratedBlueprintFile(TOMCAT_TOPOLOGY);
    }

    @Test
    public void testGenerateArtifactsTest() {
        testGeneratedBlueprintFile(ARTIFACT_TEST_TOPOLOGY);
    }

    private void overrideArtifact(PaaSTopologyDeploymentContext deploymentContext, String nodeName, String artifactId, Path newArtifactContent)
            throws IOException {
        DeploymentArtifact artifact = deploymentContext.getPaaSTopology().getAllNodes().get(nodeName).getNodeTemplate().getArtifacts().get(artifactId);
        if (ArtifactRepositoryConstants.ALIEN_ARTIFACT_REPOSITORY.equals(artifact.getArtifactRepository())) {
            artifactRepository.deleteFile(artifact.getArtifactRef());
        }
        InputStream artifactStream = Files.newInputStream(newArtifactContent);
        try {
            String artifactFileId = artifactRepository.storeFile(artifactStream);
            artifact.setArtifactName(newArtifactContent.getFileName().toString());
            artifact.setArtifactRef(artifactFileId);
            artifact.setArtifactRepository(ArtifactRepositoryConstants.ALIEN_ARTIFACT_REPOSITORY);
        } finally {
            Closeables.close(artifactStream, true);
        }
    }

    @Test
    public void testGenerateOverriddenArtifactsTest() {
        for (String location : LOCATIONS) {
            testGeneratedBlueprintFile(ARTIFACT_TEST_TOPOLOGY, location, ARTIFACT_TEST_TOPOLOGY + "Overridden", "testGenerateOverridenArtifactsTest",
                    new DeploymentContextVisitor() {
                        @Override
                        public void visitDeploymentContext(PaaSTopologyDeploymentContext context) throws Exception {
                            overrideArtifact(context, "War", "war_file", Paths.get("src/test/resources/data/war-examples/helloWorld.war"));
                        }
                    });
        }
    }

    @Test
    public void testGetComplexProperty() {
        String topology = CUSTOM_APACHE_TOPOLOGY;
        String locationName = "openstack";

        StackTraceElement[] stackTraceElements = Thread.currentThread().getStackTrace();
        if (!applicationUtil.isTopologyExistForLocation(topology, locationName)) {
            log.warn("Topology {} do not exist for location {}", topology, locationName);
            return;
        }

        PaaSTopologyDeploymentContext context = deploymentLauncher.buildPaaSDeploymentContext(stackTraceElements[2].getMethodName(), topology, locationName);

        // check the function of get_property on property
        IValue value =  context.getPaaSTopology().getNonNatives().get(0).getInterfaces().get("tosca.interfaces.node.lifecycle.Standard").getOperations().get("create").getInputParameters().get("DOC_ROOT");
        FunctionPropertyValue functionValue = (FunctionPropertyValue) value;
        assertEquals(functionValue.getFunction(), "get_property");
        assertEquals(functionValue.getParameters().get(0), "SELF");
        assertEquals(functionValue.getParameters().get(1), "floatingip");

        // check the function of get_property on capability
        IValue capabilityValue = context.getPaaSTopology().getNonNatives().get(0).getInterfaces().get("tosca.interfaces.node.lifecycle.Standard").getOperations().get("create").getInputParameters().get("GET_PROPERTY_CAPABILITY");
        FunctionPropertyValue capabilityFunctionValue = (FunctionPropertyValue) capabilityValue;
        assertEquals(capabilityFunctionValue.getFunction(), "get_property");
        assertEquals(capabilityFunctionValue.getParameters().get(0), "SELF");
        assertEquals(capabilityFunctionValue.getParameters().get(1), "host");
        assertEquals(capabilityFunctionValue.getParameters().get(2), "floatingip_capability");

        propertyEvaluatorService.processGetPropertyFunction(context);

        // check the value of get_property on property
        value =  context.getPaaSTopology().getNonNatives().get(0).getInterfaces().get("tosca.interfaces.node.lifecycle.Standard").getOperations().get("create").getInputParameters().get("DOC_ROOT");
        ScalarPropertyValue scalarValue = (ScalarPropertyValue) value;
        assertEquals(scalarValue.getValue(), "{\n  \"floating_network_name\" : \"test\"\n}");

        // check the value of get_property on capability
        capabilityValue = context.getPaaSTopology().getNonNatives().get(0).getInterfaces().get("tosca.interfaces.node.lifecycle.Standard").getOperations().get("create").getInputParameters().get("GET_PROPERTY_CAPABILITY");
        ScalarPropertyValue capabilityScalarValue = (ScalarPropertyValue) capabilityValue;
        assertEquals(capabilityScalarValue.getValue(), "{\n  \"floating_network_name\" : \"test2\"\n}");
    }
}
