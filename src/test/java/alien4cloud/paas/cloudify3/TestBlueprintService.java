package alien4cloud.paas.cloudify3;

import alien4cloud.component.repository.ArtifactLocalRepository;
import alien4cloud.component.repository.ArtifactRepositoryConstants;
import alien4cloud.model.components.DeploymentArtifact;
import alien4cloud.orchestrators.plugin.ILocationConfiguratorPlugin;
import alien4cloud.paas.cloudify3.location.AmazonLocationConfigurator;
import alien4cloud.paas.cloudify3.location.ByonLocationConfigurator;
import alien4cloud.paas.cloudify3.location.OpenstackLocationConfigurator;
import alien4cloud.paas.cloudify3.util.CSARUtil;
import alien4cloud.paas.model.PaaSTopologyDeploymentContext;
import com.google.common.io.Closeables;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Map;
import javax.annotation.PostConstruct;
import javax.annotation.Resource;
import javax.inject.Inject;
import lombok.Getter;
import lombok.extern.slf4j.Slf4j;
import org.elasticsearch.common.collect.Maps;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.context.ApplicationContext;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@Slf4j
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration("classpath:test-context.xml")
public class TestBlueprintService extends AbstractTestBlueprint {

    @Inject
    private ArtifactLocalRepository artifactRepository;

    @Inject
    private ApplicationContext applicationContext;

    /**
     * Set true to this boolean when the blueprint has changed and you want to re-register
     */
    @Getter
    protected boolean record = false;

    /**
     * Set true to this boolean so the blueprint will be uploaded to the manager to verify
     */
    @Getter
    protected boolean verifyBlueprintUpload = false;

    @Getter
    private Map<String, ILocationConfiguratorPlugin> locationsConfigurators = Maps.newHashMap();

    @Resource
    private CSARUtil csarUtil;

    @PostConstruct
    public void postConstruct() {
        LOCATIONS.add("openstack");
        locationsConfigurators.put("openstack", applicationContext.getBean(OpenstackLocationConfigurator.class));
        LOCATIONS.add("amazon");
        locationsConfigurators.put("amazon", applicationContext.getBean(AmazonLocationConfigurator.class));
        LOCATIONS.add("byon");
        locationsConfigurators.put("byon", applicationContext.getBean(ByonLocationConfigurator.class));
    }

    @Override
    public void before() throws Exception {
        super.before();
        csarUtil.uploadCSAR(Paths.get("./src/test/resources/components/artifact-test"));
        csarUtil.uploadCSAR(Paths.get("./src/test/resources/components/support-hss"));
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
        DeploymentArtifact artifact = deploymentContext.getPaaSTopology().getAllNodes().get(nodeName).getTemplate().getArtifacts().get(artifactId);
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
}
