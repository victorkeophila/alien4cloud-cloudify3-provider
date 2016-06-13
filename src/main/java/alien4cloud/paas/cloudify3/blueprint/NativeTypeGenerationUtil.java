package alien4cloud.paas.cloudify3.blueprint;

import java.nio.file.Path;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import alien4cloud.model.common.Tag;
import alien4cloud.model.components.*;
import alien4cloud.paas.cloudify3.configuration.MappingConfiguration;
import alien4cloud.paas.cloudify3.error.BadConfigurationException;
import alien4cloud.paas.cloudify3.service.PropertyEvaluatorService;
import alien4cloud.paas.cloudify3.service.model.CloudifyDeployment;
import alien4cloud.paas.cloudify3.util.mapping.IPropertyMapping;
import alien4cloud.paas.cloudify3.util.mapping.PropertiesMappingUtil;
import alien4cloud.paas.cloudify3.util.mapping.PropertyValueUtil;
import alien4cloud.tosca.serializer.ToscaPropertySerializerUtils;
import alien4cloud.utils.TagUtil;

import com.google.common.collect.Maps;

public class NativeTypeGenerationUtil extends AbstractGenerationUtil {

    public static final String MAPPED_TO_KEY = "_a4c_c3_derived_from";

    public NativeTypeGenerationUtil(MappingConfiguration mappingConfiguration, CloudifyDeployment alienDeployment, Path recipePath,
            PropertyEvaluatorService propertyEvaluatorService) {
        super(mappingConfiguration, alienDeployment, recipePath, propertyEvaluatorService);
    }

    /**
     * Utility method used by velocity generator in order to find the cloudify type from a cloudify tosca type.
     *
     * @param toscaNodeType
     *            The tosca node type.
     * @return The matching cloudify's type.
     */
    public String mapToCloudifyType(IndexedNodeType toscaNodeType) {
        String cloudifyType = TagUtil.getTagValue(toscaNodeType.getTags(), MAPPED_TO_KEY);
        if (cloudifyType == null) {
            throw new BadConfigurationException("In the type " + toscaNodeType.getElementId() + " the tag " + MAPPED_TO_KEY
                    + " is mandatory in order to know which cloudify native type to map to");
        }
        return cloudifyType;
    }

    /**
     * Apply properties mapping and then format properties for cloudify blueprint.
     *
     * @param indentLevel
     *            The indentation level for the properties.
     * @param properties
     *            The properties values map.
     * @param propMappings
     *            The mapping configuration to map values.
     * @return The formatted properties string to insert in the blueprint.
     */
    public String formatProperties(int indentLevel, Map<String, AbstractPropertyValue> properties, Map<String, List<IPropertyMapping>> propMappings) {
        Map<String, AbstractPropertyValue> mappedProperties = PropertyValueUtil.mapProperties(propMappings, properties);
        return ToscaPropertySerializerUtils.formatProperties(indentLevel, mappedProperties);
    }

    public String formatProperties(int indentLevel, Map<String, AbstractPropertyValue> properties,
            Map<String, Map<String, List<IPropertyMapping>>> propertyMappings, String nodeType) {
        Map<String, AbstractPropertyValue> mappedProperties = PropertyValueUtil.mapProperties(propertyMappings, nodeType, properties);
        return ToscaPropertySerializerUtils.formatProperties(indentLevel, mappedProperties);
    }

    public Map<String, List<IPropertyMapping>> loadPropertyMapping(IndexedNodeType type, String tagName) {
        return PropertiesMappingUtil.loadPropertyMapping(tagName, type);
    }

    public Map<String, FunctionPropertyValue> getAttributesMapping(Map<String, IValue> attributes) {
        Map<String, FunctionPropertyValue> functions = Maps.newLinkedHashMap();
        for (Map.Entry<String, IValue> attributeEntry : attributes.entrySet()) {
            if (attributeEntry.getValue() instanceof FunctionPropertyValue) {
                functions.put(attributeEntry.getKey(), (FunctionPropertyValue) attributeEntry.getValue());
            }
        }
        return functions;
    }

    /**
     * Get the value of the _a4c_persistent_resources tag.
     *
     * @param tags
     *            The list of tags in which to search.
     * @return The value of the _a4c_persistent_resources tag or null if the tag is not present in the list.
     */
    public String getPersistentResourceId(List<Tag> tags) {
        return TagUtil.getTagValue(tags, CustomTags.PERSISTENT_RESOURCE_TAG);
    }

}
