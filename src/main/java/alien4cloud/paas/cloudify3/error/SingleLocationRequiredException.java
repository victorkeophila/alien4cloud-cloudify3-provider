package alien4cloud.paas.cloudify3.error;

/**
 * Cloudify 3 doesn't support a deployment with more or less than a single location.
 */
public class SingleLocationRequiredException extends RuntimeException {
}
