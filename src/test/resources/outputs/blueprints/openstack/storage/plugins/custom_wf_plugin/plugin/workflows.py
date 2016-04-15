from cloudify.decorators import workflow
from cloudify.workflows import ctx
from cloudify.workflows import tasks as workflow_tasks
from utils import set_state_task
from utils import operation_task
from utils import link_tasks
from utils import CustomContext
from utils import generate_native_node_workflows
from utils import _get_all_nodes
from utils import _get_all_nodes_instances
from utils import _get_all_modified_node_instances
from utils import is_host_node
from workflow import WfStartEvent
from workflow import build_pre_event


# subworkflow 'install' for host 'Compute'
def install_host_compute(ctx, graph, custom_context):
    custom_context.add_customized_wf_node('LinuxFileSystem-4')
    custom_context.add_customized_wf_node('LinuxFileSystem-2')
    custom_context.add_customized_wf_node('LinuxFileSystem-3')
    custom_context.add_customized_wf_node('LinuxFileSystem-4')
    custom_context.add_customized_wf_node('LinuxFileSystem-4')
    custom_context.add_customized_wf_node('LinuxFileSystem-3')
    custom_context.add_customized_wf_node('LinuxFileSystem-2')
    custom_context.add_customized_wf_node('LinuxFileSystem-1')
    custom_context.add_customized_wf_node('LinuxFileSystem-1')
    custom_context.add_customized_wf_node('LinuxFileSystem-2')
    custom_context.add_customized_wf_node('LinuxFileSystem-4')
    custom_context.add_customized_wf_node('LinuxFileSystem-2')
    custom_context.add_customized_wf_node('LinuxFileSystem-2')
    custom_context.add_customized_wf_node('LinuxFileSystem-1')
    custom_context.add_customized_wf_node('LinuxFileSystem-2')
    custom_context.add_customized_wf_node('LinuxFileSystem-1')
    custom_context.add_customized_wf_node('LinuxFileSystem-1')
    custom_context.add_customized_wf_node('LinuxFileSystem-1')
    custom_context.add_customized_wf_node('LinuxFileSystem-3')
    custom_context.add_customized_wf_node('LinuxFileSystem-4')
    custom_context.add_customized_wf_node('LinuxFileSystem-3')
    custom_context.add_customized_wf_node('LinuxFileSystem-3')
    custom_context.add_customized_wf_node('LinuxFileSystem-4')
    custom_context.add_customized_wf_node('LinuxFileSystem-2')
    custom_context.add_customized_wf_node('LinuxFileSystem-4')
    custom_context.add_customized_wf_node('LinuxFileSystem-3')
    custom_context.add_customized_wf_node('LinuxFileSystem-3')
    custom_context.add_customized_wf_node('LinuxFileSystem-1')
    set_state_task(ctx, graph, 'LinuxFileSystem-4', 'configuring', 'LinuxFileSystem-4_configuring', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-2', 'starting', 'LinuxFileSystem-2_starting', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-3', 'configured', 'LinuxFileSystem-3_configured', custom_context)
    custom_context.register_native_delegate_wf_step('Compute', 'Compute_install')
    set_state_task(ctx, graph, 'LinuxFileSystem-4', 'creating', 'LinuxFileSystem-4_creating', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-4', 'started', 'LinuxFileSystem-4_started', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-3', 'creating', 'LinuxFileSystem-3_creating', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-2', 'creating', 'LinuxFileSystem-2_creating', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-1', 'started', 'LinuxFileSystem-1_started', custom_context)
    operation_task(ctx, graph, 'LinuxFileSystem-2', 'cloudify.interfaces.lifecycle.start', 'start_LinuxFileSystem-2', custom_context)
    operation_task(ctx, graph, 'LinuxFileSystem-1', 'cloudify.interfaces.lifecycle.start', 'start_LinuxFileSystem-1', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-1', 'starting', 'LinuxFileSystem-1_starting', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-2', 'created', 'LinuxFileSystem-2_created', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-4', 'created', 'LinuxFileSystem-4_created', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-2', 'started', 'LinuxFileSystem-2_started', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-2', 'configured', 'LinuxFileSystem-2_configured', custom_context)
    operation_task(ctx, graph, 'LinuxFileSystem-4', 'cloudify.interfaces.lifecycle.configure', 'configure_LinuxFileSystem-4', custom_context)
    operation_task(ctx, graph, 'LinuxFileSystem-3', 'cloudify.interfaces.lifecycle.configure', 'configure_LinuxFileSystem-3', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-1', 'configuring', 'LinuxFileSystem-1_configuring', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-2', 'initial', 'LinuxFileSystem-2_initial', custom_context)
    operation_task(ctx, graph, 'LinuxFileSystem-4', 'cloudify.interfaces.lifecycle.start', 'start_LinuxFileSystem-4', custom_context)
    operation_task(ctx, graph, 'LinuxFileSystem-2', 'cloudify.interfaces.lifecycle.configure', 'configure_LinuxFileSystem-2', custom_context)
    operation_task(ctx, graph, 'LinuxFileSystem-3', 'cloudify.interfaces.lifecycle.start', 'start_LinuxFileSystem-3', custom_context)
    operation_task(ctx, graph, 'LinuxFileSystem-1', 'cloudify.interfaces.lifecycle.configure', 'configure_LinuxFileSystem-1', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-1', 'created', 'LinuxFileSystem-1_created', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-1', 'creating', 'LinuxFileSystem-1_creating', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-1', 'initial', 'LinuxFileSystem-1_initial', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-3', 'initial', 'LinuxFileSystem-3_initial', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-4', 'configured', 'LinuxFileSystem-4_configured', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-3', 'started', 'LinuxFileSystem-3_started', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-3', 'created', 'LinuxFileSystem-3_created', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-4', 'starting', 'LinuxFileSystem-4_starting', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-2', 'configuring', 'LinuxFileSystem-2_configuring', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-4', 'initial', 'LinuxFileSystem-4_initial', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-3', 'configuring', 'LinuxFileSystem-3_configuring', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-3', 'starting', 'LinuxFileSystem-3_starting', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-1', 'configured', 'LinuxFileSystem-1_configured', custom_context)
    generate_native_node_workflows(ctx, graph, custom_context, 'install')
    link_tasks(graph, 'configure_LinuxFileSystem-4', 'LinuxFileSystem-4_configuring', custom_context)
    link_tasks(graph, 'start_LinuxFileSystem-2', 'LinuxFileSystem-2_starting', custom_context)
    link_tasks(graph, 'LinuxFileSystem-3_starting', 'LinuxFileSystem-3_configured', custom_context)
    link_tasks(graph, 'LinuxFileSystem-3_initial', 'Compute_install', custom_context)
    link_tasks(graph, 'LinuxFileSystem-4_initial', 'Compute_install', custom_context)
    link_tasks(graph, 'LinuxFileSystem-2_initial', 'Compute_install', custom_context)
    link_tasks(graph, 'LinuxFileSystem-1_initial', 'Compute_install', custom_context)
    link_tasks(graph, 'LinuxFileSystem-4_created', 'LinuxFileSystem-4_creating', custom_context)
    link_tasks(graph, 'LinuxFileSystem-3_created', 'LinuxFileSystem-3_creating', custom_context)
    link_tasks(graph, 'LinuxFileSystem-2_created', 'LinuxFileSystem-2_creating', custom_context)
    link_tasks(graph, 'LinuxFileSystem-2_started', 'start_LinuxFileSystem-2', custom_context)
    link_tasks(graph, 'LinuxFileSystem-1_started', 'start_LinuxFileSystem-1', custom_context)
    link_tasks(graph, 'start_LinuxFileSystem-1', 'LinuxFileSystem-1_starting', custom_context)
    link_tasks(graph, 'LinuxFileSystem-2_configuring', 'LinuxFileSystem-2_created', custom_context)
    link_tasks(graph, 'LinuxFileSystem-4_configuring', 'LinuxFileSystem-4_created', custom_context)
    link_tasks(graph, 'LinuxFileSystem-2_starting', 'LinuxFileSystem-2_configured', custom_context)
    link_tasks(graph, 'LinuxFileSystem-4_configured', 'configure_LinuxFileSystem-4', custom_context)
    link_tasks(graph, 'LinuxFileSystem-3_configured', 'configure_LinuxFileSystem-3', custom_context)
    link_tasks(graph, 'configure_LinuxFileSystem-1', 'LinuxFileSystem-1_configuring', custom_context)
    link_tasks(graph, 'LinuxFileSystem-2_creating', 'LinuxFileSystem-2_initial', custom_context)
    link_tasks(graph, 'LinuxFileSystem-4_started', 'start_LinuxFileSystem-4', custom_context)
    link_tasks(graph, 'LinuxFileSystem-2_configured', 'configure_LinuxFileSystem-2', custom_context)
    link_tasks(graph, 'LinuxFileSystem-3_started', 'start_LinuxFileSystem-3', custom_context)
    link_tasks(graph, 'LinuxFileSystem-1_configured', 'configure_LinuxFileSystem-1', custom_context)
    link_tasks(graph, 'LinuxFileSystem-1_configuring', 'LinuxFileSystem-1_created', custom_context)
    link_tasks(graph, 'LinuxFileSystem-1_created', 'LinuxFileSystem-1_creating', custom_context)
    link_tasks(graph, 'LinuxFileSystem-1_creating', 'LinuxFileSystem-1_initial', custom_context)
    link_tasks(graph, 'LinuxFileSystem-3_creating', 'LinuxFileSystem-3_initial', custom_context)
    link_tasks(graph, 'LinuxFileSystem-4_starting', 'LinuxFileSystem-4_configured', custom_context)
    link_tasks(graph, 'LinuxFileSystem-3_configuring', 'LinuxFileSystem-3_created', custom_context)
    link_tasks(graph, 'start_LinuxFileSystem-4', 'LinuxFileSystem-4_starting', custom_context)
    link_tasks(graph, 'configure_LinuxFileSystem-2', 'LinuxFileSystem-2_configuring', custom_context)
    link_tasks(graph, 'LinuxFileSystem-4_creating', 'LinuxFileSystem-4_initial', custom_context)
    link_tasks(graph, 'configure_LinuxFileSystem-3', 'LinuxFileSystem-3_configuring', custom_context)
    link_tasks(graph, 'start_LinuxFileSystem-3', 'LinuxFileSystem-3_starting', custom_context)
    link_tasks(graph, 'LinuxFileSystem-1_starting', 'LinuxFileSystem-1_configured', custom_context)


# subworkflow 'uninstall' for host 'Compute'
def uninstall_host_compute(ctx, graph, custom_context):
    custom_context.add_customized_wf_node('LinuxFileSystem-2')
    custom_context.add_customized_wf_node('LinuxFileSystem-1')
    custom_context.add_customized_wf_node('LinuxFileSystem-3')
    custom_context.add_customized_wf_node('LinuxFileSystem-4')
    custom_context.add_customized_wf_node('LinuxFileSystem-1')
    custom_context.add_customized_wf_node('LinuxFileSystem-4')
    custom_context.add_customized_wf_node('LinuxFileSystem-3')
    custom_context.add_customized_wf_node('LinuxFileSystem-3')
    custom_context.add_customized_wf_node('LinuxFileSystem-4')
    custom_context.add_customized_wf_node('LinuxFileSystem-2')
    custom_context.add_customized_wf_node('LinuxFileSystem-2')
    custom_context.add_customized_wf_node('LinuxFileSystem-3')
    custom_context.add_customized_wf_node('LinuxFileSystem-1')
    custom_context.add_customized_wf_node('LinuxFileSystem-2')
    custom_context.add_customized_wf_node('LinuxFileSystem-1')
    custom_context.add_customized_wf_node('LinuxFileSystem-4')
    set_state_task(ctx, graph, 'LinuxFileSystem-2', 'stopping', 'LinuxFileSystem-2_stopping', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-1', 'deleting', 'LinuxFileSystem-1_deleting', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-3', 'deleted', 'LinuxFileSystem-3_deleted', custom_context)
    custom_context.register_native_delegate_wf_step('Compute', 'Compute_uninstall')
    set_state_task(ctx, graph, 'LinuxFileSystem-4', 'deleting', 'LinuxFileSystem-4_deleting', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-1', 'stopped', 'LinuxFileSystem-1_stopped', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-4', 'stopped', 'LinuxFileSystem-4_stopped', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-3', 'deleting', 'LinuxFileSystem-3_deleting', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-3', 'stopped', 'LinuxFileSystem-3_stopped', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-4', 'deleted', 'LinuxFileSystem-4_deleted', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-2', 'deleted', 'LinuxFileSystem-2_deleted', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-2', 'deleting', 'LinuxFileSystem-2_deleting', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-3', 'stopping', 'LinuxFileSystem-3_stopping', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-1', 'deleted', 'LinuxFileSystem-1_deleted', custom_context)
    operation_task(ctx, graph, 'LinuxFileSystem-1', 'cloudify.interfaces.lifecycle.stop', 'stop_LinuxFileSystem-1', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-2', 'stopped', 'LinuxFileSystem-2_stopped', custom_context)
    operation_task(ctx, graph, 'LinuxFileSystem-2', 'cloudify.interfaces.lifecycle.stop', 'stop_LinuxFileSystem-2', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-1', 'stopping', 'LinuxFileSystem-1_stopping', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-4', 'stopping', 'LinuxFileSystem-4_stopping', custom_context)
    operation_task(ctx, graph, 'LinuxFileSystem-3', 'cloudify.interfaces.lifecycle.stop', 'stop_LinuxFileSystem-3', custom_context)
    operation_task(ctx, graph, 'LinuxFileSystem-4', 'cloudify.interfaces.lifecycle.stop', 'stop_LinuxFileSystem-4', custom_context)
    generate_native_node_workflows(ctx, graph, custom_context, 'uninstall')
    link_tasks(graph, 'stop_LinuxFileSystem-2', 'LinuxFileSystem-2_stopping', custom_context)
    link_tasks(graph, 'LinuxFileSystem-1_deleted', 'LinuxFileSystem-1_deleting', custom_context)
    link_tasks(graph, 'Compute_uninstall', 'LinuxFileSystem-3_deleted', custom_context)
    link_tasks(graph, 'LinuxFileSystem-4_deleted', 'LinuxFileSystem-4_deleting', custom_context)
    link_tasks(graph, 'LinuxFileSystem-1_deleting', 'LinuxFileSystem-1_stopped', custom_context)
    link_tasks(graph, 'LinuxFileSystem-4_deleting', 'LinuxFileSystem-4_stopped', custom_context)
    link_tasks(graph, 'LinuxFileSystem-3_deleted', 'LinuxFileSystem-3_deleting', custom_context)
    link_tasks(graph, 'LinuxFileSystem-3_deleting', 'LinuxFileSystem-3_stopped', custom_context)
    link_tasks(graph, 'Compute_uninstall', 'LinuxFileSystem-4_deleted', custom_context)
    link_tasks(graph, 'Compute_uninstall', 'LinuxFileSystem-2_deleted', custom_context)
    link_tasks(graph, 'LinuxFileSystem-2_deleted', 'LinuxFileSystem-2_deleting', custom_context)
    link_tasks(graph, 'stop_LinuxFileSystem-3', 'LinuxFileSystem-3_stopping', custom_context)
    link_tasks(graph, 'Compute_uninstall', 'LinuxFileSystem-1_deleted', custom_context)
    link_tasks(graph, 'LinuxFileSystem-1_stopped', 'stop_LinuxFileSystem-1', custom_context)
    link_tasks(graph, 'LinuxFileSystem-2_deleting', 'LinuxFileSystem-2_stopped', custom_context)
    link_tasks(graph, 'LinuxFileSystem-2_stopped', 'stop_LinuxFileSystem-2', custom_context)
    link_tasks(graph, 'stop_LinuxFileSystem-1', 'LinuxFileSystem-1_stopping', custom_context)
    link_tasks(graph, 'stop_LinuxFileSystem-4', 'LinuxFileSystem-4_stopping', custom_context)
    link_tasks(graph, 'LinuxFileSystem-3_stopped', 'stop_LinuxFileSystem-3', custom_context)
    link_tasks(graph, 'LinuxFileSystem-4_stopped', 'stop_LinuxFileSystem-4', custom_context)


def install_host(ctx, graph, custom_context, compute):
    options = {}
    options['Compute'] = install_host_compute
    options[compute](ctx, graph, custom_context)


def uninstall_host(ctx, graph, custom_context, compute):
    options = {}
    options['Compute'] = uninstall_host_compute
    options[compute](ctx, graph, custom_context)


@workflow
def a4c_install(**kwargs):
    graph = ctx.graph_mode()
    nodes = _get_all_nodes(ctx)
    instances = _get_all_nodes_instances(ctx)
    custom_context = CustomContext(ctx, instances, nodes)
    ctx.internal.send_workflow_event(event_type='a4c_workflow_started', message=build_pre_event(WfStartEvent('install')))
    _a4c_install(ctx, graph, custom_context)
    return graph.execute()


@workflow
def a4c_uninstall(**kwargs):
    graph = ctx.graph_mode()
    nodes = _get_all_nodes(ctx)
    instances = _get_all_nodes_instances(ctx)
    custom_context = CustomContext(ctx, instances, nodes)
    ctx.internal.send_workflow_event(event_type='a4c_workflow_started', message=build_pre_event(WfStartEvent('uninstall')))
    _a4c_uninstall(ctx, graph, custom_context)
    return graph.execute()


def _a4c_install(ctx, graph, custom_context):
    #  following code can be pasted in src/test/python/workflows/tasks.py for simulation
    custom_context.add_customized_wf_node('LinuxFileSystem-4')
    custom_context.add_customized_wf_node('LinuxFileSystem-2')
    custom_context.add_customized_wf_node('LinuxFileSystem-3')
    custom_context.add_customized_wf_node('LinuxFileSystem-4')
    custom_context.add_customized_wf_node('LinuxFileSystem-4')
    custom_context.add_customized_wf_node('LinuxFileSystem-3')
    custom_context.add_customized_wf_node('LinuxFileSystem-2')
    custom_context.add_customized_wf_node('LinuxFileSystem-1')
    custom_context.add_customized_wf_node('LinuxFileSystem-1')
    custom_context.add_customized_wf_node('LinuxFileSystem-2')
    custom_context.add_customized_wf_node('LinuxFileSystem-4')
    custom_context.add_customized_wf_node('LinuxFileSystem-2')
    custom_context.add_customized_wf_node('LinuxFileSystem-2')
    custom_context.add_customized_wf_node('LinuxFileSystem-1')
    custom_context.add_customized_wf_node('LinuxFileSystem-2')
    custom_context.add_customized_wf_node('LinuxFileSystem-1')
    custom_context.add_customized_wf_node('LinuxFileSystem-1')
    custom_context.add_customized_wf_node('LinuxFileSystem-1')
    custom_context.add_customized_wf_node('LinuxFileSystem-3')
    custom_context.add_customized_wf_node('LinuxFileSystem-4')
    custom_context.add_customized_wf_node('LinuxFileSystem-3')
    custom_context.add_customized_wf_node('LinuxFileSystem-3')
    custom_context.add_customized_wf_node('LinuxFileSystem-4')
    custom_context.add_customized_wf_node('LinuxFileSystem-2')
    custom_context.add_customized_wf_node('LinuxFileSystem-4')
    custom_context.add_customized_wf_node('LinuxFileSystem-3')
    custom_context.add_customized_wf_node('LinuxFileSystem-3')
    custom_context.add_customized_wf_node('LinuxFileSystem-1')
    set_state_task(ctx, graph, 'LinuxFileSystem-4', 'configuring', 'LinuxFileSystem-4_configuring', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-2', 'starting', 'LinuxFileSystem-2_starting', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-3', 'configured', 'LinuxFileSystem-3_configured', custom_context)
    custom_context.register_native_delegate_wf_step('Compute', 'Compute_install')
    set_state_task(ctx, graph, 'LinuxFileSystem-4', 'creating', 'LinuxFileSystem-4_creating', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-4', 'started', 'LinuxFileSystem-4_started', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-3', 'creating', 'LinuxFileSystem-3_creating', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-2', 'creating', 'LinuxFileSystem-2_creating', custom_context)
    custom_context.register_native_delegate_wf_step('CBS2', 'CBS2_install')
    set_state_task(ctx, graph, 'LinuxFileSystem-1', 'started', 'LinuxFileSystem-1_started', custom_context)
    operation_task(ctx, graph, 'LinuxFileSystem-2', 'cloudify.interfaces.lifecycle.start', 'start_LinuxFileSystem-2', custom_context)
    operation_task(ctx, graph, 'LinuxFileSystem-1', 'cloudify.interfaces.lifecycle.start', 'start_LinuxFileSystem-1', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-1', 'starting', 'LinuxFileSystem-1_starting', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-2', 'created', 'LinuxFileSystem-2_created', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-4', 'created', 'LinuxFileSystem-4_created', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-2', 'started', 'LinuxFileSystem-2_started', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-2', 'configured', 'LinuxFileSystem-2_configured', custom_context)
    operation_task(ctx, graph, 'LinuxFileSystem-4', 'cloudify.interfaces.lifecycle.configure', 'configure_LinuxFileSystem-4', custom_context)
    operation_task(ctx, graph, 'LinuxFileSystem-3', 'cloudify.interfaces.lifecycle.configure', 'configure_LinuxFileSystem-3', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-1', 'configuring', 'LinuxFileSystem-1_configuring', custom_context)
    custom_context.register_native_delegate_wf_step('CBS3', 'CBS3_install')
    set_state_task(ctx, graph, 'LinuxFileSystem-2', 'initial', 'LinuxFileSystem-2_initial', custom_context)
    operation_task(ctx, graph, 'LinuxFileSystem-4', 'cloudify.interfaces.lifecycle.start', 'start_LinuxFileSystem-4', custom_context)
    operation_task(ctx, graph, 'LinuxFileSystem-2', 'cloudify.interfaces.lifecycle.configure', 'configure_LinuxFileSystem-2', custom_context)
    operation_task(ctx, graph, 'LinuxFileSystem-3', 'cloudify.interfaces.lifecycle.start', 'start_LinuxFileSystem-3', custom_context)
    operation_task(ctx, graph, 'LinuxFileSystem-1', 'cloudify.interfaces.lifecycle.configure', 'configure_LinuxFileSystem-1', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-1', 'created', 'LinuxFileSystem-1_created', custom_context)
    custom_context.register_native_delegate_wf_step('CBS1', 'CBS1_install')
    set_state_task(ctx, graph, 'LinuxFileSystem-1', 'creating', 'LinuxFileSystem-1_creating', custom_context)
    custom_context.register_native_delegate_wf_step('PublicNetwork', 'PublicNetwork_install')
    set_state_task(ctx, graph, 'LinuxFileSystem-1', 'initial', 'LinuxFileSystem-1_initial', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-3', 'initial', 'LinuxFileSystem-3_initial', custom_context)
    custom_context.register_native_delegate_wf_step('CBS4', 'CBS4_install')
    set_state_task(ctx, graph, 'LinuxFileSystem-4', 'configured', 'LinuxFileSystem-4_configured', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-3', 'started', 'LinuxFileSystem-3_started', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-3', 'created', 'LinuxFileSystem-3_created', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-4', 'starting', 'LinuxFileSystem-4_starting', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-2', 'configuring', 'LinuxFileSystem-2_configuring', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-4', 'initial', 'LinuxFileSystem-4_initial', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-3', 'configuring', 'LinuxFileSystem-3_configuring', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-3', 'starting', 'LinuxFileSystem-3_starting', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-1', 'configured', 'LinuxFileSystem-1_configured', custom_context)
    generate_native_node_workflows(ctx, graph, custom_context, 'install')
    link_tasks(graph, 'LinuxFileSystem-4_configuring', 'LinuxFileSystem-4_created', custom_context)
    link_tasks(graph, 'LinuxFileSystem-2_starting', 'LinuxFileSystem-2_configured', custom_context)
    link_tasks(graph, 'LinuxFileSystem-3_configured', 'configure_LinuxFileSystem-3', custom_context)
    link_tasks(graph, 'LinuxFileSystem-4_creating', 'LinuxFileSystem-4_initial', custom_context)
    link_tasks(graph, 'LinuxFileSystem-4_started', 'start_LinuxFileSystem-4', custom_context)
    link_tasks(graph, 'LinuxFileSystem-3_creating', 'LinuxFileSystem-3_initial', custom_context)
    link_tasks(graph, 'LinuxFileSystem-2_creating', 'LinuxFileSystem-2_initial', custom_context)
    link_tasks(graph, 'LinuxFileSystem-1_started', 'start_LinuxFileSystem-1', custom_context)
    link_tasks(graph, 'start_LinuxFileSystem-2', 'LinuxFileSystem-2_starting', custom_context)
    link_tasks(graph, 'start_LinuxFileSystem-1', 'LinuxFileSystem-1_starting', custom_context)
    link_tasks(graph, 'LinuxFileSystem-1_starting', 'LinuxFileSystem-1_configured', custom_context)
    link_tasks(graph, 'LinuxFileSystem-2_created', 'LinuxFileSystem-2_creating', custom_context)
    link_tasks(graph, 'LinuxFileSystem-4_created', 'LinuxFileSystem-4_creating', custom_context)
    link_tasks(graph, 'LinuxFileSystem-2_started', 'start_LinuxFileSystem-2', custom_context)
    link_tasks(graph, 'LinuxFileSystem-2_configured', 'configure_LinuxFileSystem-2', custom_context)
    link_tasks(graph, 'configure_LinuxFileSystem-4', 'LinuxFileSystem-4_configuring', custom_context)
    link_tasks(graph, 'configure_LinuxFileSystem-3', 'LinuxFileSystem-3_configuring', custom_context)
    link_tasks(graph, 'LinuxFileSystem-1_configuring', 'LinuxFileSystem-1_created', custom_context)
    link_tasks(graph, 'LinuxFileSystem-2_initial', 'CBS2_install', custom_context)
    link_tasks(graph, 'LinuxFileSystem-2_initial', 'Compute_install', custom_context)
    link_tasks(graph, 'start_LinuxFileSystem-4', 'LinuxFileSystem-4_starting', custom_context)
    link_tasks(graph, 'configure_LinuxFileSystem-2', 'LinuxFileSystem-2_configuring', custom_context)
    link_tasks(graph, 'start_LinuxFileSystem-3', 'LinuxFileSystem-3_starting', custom_context)
    link_tasks(graph, 'configure_LinuxFileSystem-1', 'LinuxFileSystem-1_configuring', custom_context)
    link_tasks(graph, 'LinuxFileSystem-1_created', 'LinuxFileSystem-1_creating', custom_context)
    link_tasks(graph, 'LinuxFileSystem-1_creating', 'LinuxFileSystem-1_initial', custom_context)
    link_tasks(graph, 'LinuxFileSystem-1_initial', 'CBS1_install', custom_context)
    link_tasks(graph, 'LinuxFileSystem-1_initial', 'Compute_install', custom_context)
    link_tasks(graph, 'LinuxFileSystem-3_initial', 'CBS3_install', custom_context)
    link_tasks(graph, 'LinuxFileSystem-3_initial', 'Compute_install', custom_context)
    link_tasks(graph, 'LinuxFileSystem-4_configured', 'configure_LinuxFileSystem-4', custom_context)
    link_tasks(graph, 'LinuxFileSystem-3_started', 'start_LinuxFileSystem-3', custom_context)
    link_tasks(graph, 'LinuxFileSystem-3_created', 'LinuxFileSystem-3_creating', custom_context)
    link_tasks(graph, 'LinuxFileSystem-4_starting', 'LinuxFileSystem-4_configured', custom_context)
    link_tasks(graph, 'LinuxFileSystem-2_configuring', 'LinuxFileSystem-2_created', custom_context)
    link_tasks(graph, 'LinuxFileSystem-4_initial', 'CBS4_install', custom_context)
    link_tasks(graph, 'LinuxFileSystem-4_initial', 'Compute_install', custom_context)
    link_tasks(graph, 'LinuxFileSystem-3_configuring', 'LinuxFileSystem-3_created', custom_context)
    link_tasks(graph, 'LinuxFileSystem-3_starting', 'LinuxFileSystem-3_configured', custom_context)
    link_tasks(graph, 'LinuxFileSystem-1_configured', 'configure_LinuxFileSystem-1', custom_context)


@workflow
def a4c_scale(ctx, node_id, delta, scale_compute, **kwargs):
    scaled_node = ctx.get_node(node_id)
    if not scaled_node:
        raise ValueError("Node {0} doesn't exist".format(node_id))
    if not is_host_node(scaled_node):
        raise ValueError("Node {0} is not a host. This workflow can only scale hosts".format(node_id))
    if delta == 0:
        ctx.logger.info('delta parameter is 0, so no scaling will take place.')
        return

    curr_num_instances = scaled_node.number_of_instances
    planned_num_instances = curr_num_instances + delta
    if planned_num_instances < 1:
        raise ValueError('Provided delta: {0} is illegal. current number of'
                         'instances of node {1} is {2}'
                         .format(delta, node_id, curr_num_instances))

    modification = ctx.deployment.start_modification({
        scaled_node.id: {
            'instances': planned_num_instances
        }
    })
    ctx.logger.info(
        'Deployment modification started. [modification_id={0} : {1}]'.format(modification.id, dir(modification)))
    try:
        if delta > 0:
            ctx.logger.info('Scaling host {0} adding {1} instances'.format(node_id, delta))
            added_and_related = _get_all_nodes(modification.added)
            added = _get_all_modified_node_instances(added_and_related, 'added')
            graph = ctx.graph_mode()
            ctx.internal.send_workflow_event(event_type='a4c_workflow_started',
                                             message=build_pre_event(WfStartEvent('scale', 'install')))
            custom_context = CustomContext(ctx, added, added_and_related)
            install_host(ctx, graph, custom_context, node_id)
            try:
                graph.execute()
            except:
                ctx.logger.error('Scale failed. Uninstalling node {0}'.format(node_id))
                graph = ctx.internal.task_graph
                for task in graph.tasks_iter():
                    graph.remove_task(task)
                try:
                    custom_context = CustomContext(ctx, added, added_and_related)
                    uninstall_host(ctx, graph, custom_context, node_id)
                    graph.execute()
                except:
                    ctx.logger.error('Node {0} uninstallation following scale failure has failed'.format(node_id))
                raise
        else:
            ctx.logger.info('Unscaling host {0} removing {1} instances'.format(node_id, delta))
            removed_and_related = _get_all_nodes(modification.removed)
            removed = _get_all_modified_node_instances(removed_and_related, 'removed')
            graph = ctx.graph_mode()
            ctx.internal.send_workflow_event(event_type='a4c_workflow_started',
                                             message=build_pre_event(WfStartEvent('scale', 'uninstall')))
            custom_context = CustomContext(ctx, removed, removed_and_related)
            uninstall_host(ctx, graph, custom_context, node_id)
            try:
                graph.execute()
            except:
                ctx.logger.error('Unscale failed.')
                raise
    except:
        ctx.logger.warn('Rolling back deployment modification. [modification_id={0}]'.format(modification.id))
        try:
            modification.rollback()
        except:
            ctx.logger.warn('Deployment modification rollback failed. The '
                            'deployment model is most likely in some corrupted'
                            ' state.'
                            '[modification_id={0}]'.format(modification.id))
            raise
        raise
    else:
        try:
            modification.finish()
        except:
            ctx.logger.warn('Deployment modification finish failed. The '
                            'deployment model is most likely in some corrupted'
                            ' state.'
                            '[modification_id={0}]'.format(modification.id))
            raise


@workflow
def a4c_heal(
        ctx,
        node_instance_id,
        diagnose_value='Not provided',
        **kwargs):
    """Reinstalls the whole subgraph of the system topology

    The subgraph consists of all the nodes that are hosted in the
    failing node's compute and the compute itself.
    Additionally it unlinks and establishes appropriate relationships

    :param ctx: cloudify context
    :param node_id: failing node's id
    :param diagnose_value: diagnosed reason of failure
    """

    ctx.logger.info("Starting 'heal' workflow on {0}, Diagnosis: {1}"
                    .format(node_instance_id, diagnose_value))
    failing_node = ctx.get_node_instance(node_instance_id)
    host_instance_id = failing_node._node_instance.host_id
    failing_node_host = ctx.get_node_instance(host_instance_id)
    node_id = failing_node_host.node_id
    subgraph_node_instances = failing_node_host.get_contained_subgraph()
    added_and_related = _get_all_nodes(ctx)
    try:
      graph = ctx.graph_mode()
      ctx.internal.send_workflow_event(event_type='a4c_workflow_started',
                                               message=build_pre_event(WfStartEvent('heal', 'uninstall')))
      custom_context = CustomContext(ctx, subgraph_node_instances, added_and_related)
      uninstall_host(ctx, graph, custom_context, node_id)
      graph.execute()
    except:
      ctx.logger.error('Uninstall while healing failed.')
    graph = ctx.internal.task_graph
    for task in graph.tasks_iter():
      graph.remove_task(task)
    ctx.internal.send_workflow_event(event_type='a4c_workflow_started',
                                             message=build_pre_event(WfStartEvent('heal', 'install')))
    custom_context = CustomContext(ctx, subgraph_node_instances, added_and_related)
    install_host(ctx, graph, custom_context, node_id)
    graph.execute()


def _a4c_uninstall(ctx, graph, custom_context):
    #  following code can be pasted in src/test/python/workflows/tasks.py for simulation
    custom_context.add_customized_wf_node('LinuxFileSystem-2')
    custom_context.add_customized_wf_node('LinuxFileSystem-1')
    custom_context.add_customized_wf_node('LinuxFileSystem-3')
    custom_context.add_customized_wf_node('LinuxFileSystem-4')
    custom_context.add_customized_wf_node('LinuxFileSystem-1')
    custom_context.add_customized_wf_node('LinuxFileSystem-4')
    custom_context.add_customized_wf_node('LinuxFileSystem-3')
    custom_context.add_customized_wf_node('LinuxFileSystem-3')
    custom_context.add_customized_wf_node('LinuxFileSystem-4')
    custom_context.add_customized_wf_node('LinuxFileSystem-2')
    custom_context.add_customized_wf_node('LinuxFileSystem-2')
    custom_context.add_customized_wf_node('LinuxFileSystem-3')
    custom_context.add_customized_wf_node('LinuxFileSystem-1')
    custom_context.add_customized_wf_node('LinuxFileSystem-2')
    custom_context.add_customized_wf_node('LinuxFileSystem-1')
    custom_context.add_customized_wf_node('LinuxFileSystem-4')
    set_state_task(ctx, graph, 'LinuxFileSystem-2', 'stopping', 'LinuxFileSystem-2_stopping', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-1', 'deleting', 'LinuxFileSystem-1_deleting', custom_context)
    custom_context.register_native_delegate_wf_step('CBS1', 'CBS1_uninstall')
    set_state_task(ctx, graph, 'LinuxFileSystem-3', 'deleted', 'LinuxFileSystem-3_deleted', custom_context)
    custom_context.register_native_delegate_wf_step('Compute', 'Compute_uninstall')
    set_state_task(ctx, graph, 'LinuxFileSystem-4', 'deleting', 'LinuxFileSystem-4_deleting', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-1', 'stopped', 'LinuxFileSystem-1_stopped', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-4', 'stopped', 'LinuxFileSystem-4_stopped', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-3', 'deleting', 'LinuxFileSystem-3_deleting', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-3', 'stopped', 'LinuxFileSystem-3_stopped', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-4', 'deleted', 'LinuxFileSystem-4_deleted', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-2', 'deleted', 'LinuxFileSystem-2_deleted', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-2', 'deleting', 'LinuxFileSystem-2_deleting', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-3', 'stopping', 'LinuxFileSystem-3_stopping', custom_context)
    custom_context.register_native_delegate_wf_step('CBS3', 'CBS3_uninstall')
    custom_context.register_native_delegate_wf_step('CBS4', 'CBS4_uninstall')
    set_state_task(ctx, graph, 'LinuxFileSystem-1', 'deleted', 'LinuxFileSystem-1_deleted', custom_context)
    custom_context.register_native_delegate_wf_step('PublicNetwork', 'PublicNetwork_uninstall')
    operation_task(ctx, graph, 'LinuxFileSystem-1', 'cloudify.interfaces.lifecycle.stop', 'stop_LinuxFileSystem-1', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-2', 'stopped', 'LinuxFileSystem-2_stopped', custom_context)
    operation_task(ctx, graph, 'LinuxFileSystem-2', 'cloudify.interfaces.lifecycle.stop', 'stop_LinuxFileSystem-2', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-1', 'stopping', 'LinuxFileSystem-1_stopping', custom_context)
    set_state_task(ctx, graph, 'LinuxFileSystem-4', 'stopping', 'LinuxFileSystem-4_stopping', custom_context)
    operation_task(ctx, graph, 'LinuxFileSystem-3', 'cloudify.interfaces.lifecycle.stop', 'stop_LinuxFileSystem-3', custom_context)
    operation_task(ctx, graph, 'LinuxFileSystem-4', 'cloudify.interfaces.lifecycle.stop', 'stop_LinuxFileSystem-4', custom_context)
    custom_context.register_native_delegate_wf_step('CBS2', 'CBS2_uninstall')
    generate_native_node_workflows(ctx, graph, custom_context, 'uninstall')
    link_tasks(graph, 'LinuxFileSystem-1_deleting', 'LinuxFileSystem-1_stopped', custom_context)
    link_tasks(graph, 'CBS1_uninstall', 'LinuxFileSystem-1_deleted', custom_context)
    link_tasks(graph, 'LinuxFileSystem-3_deleted', 'LinuxFileSystem-3_deleting', custom_context)
    link_tasks(graph, 'Compute_uninstall', 'LinuxFileSystem-4_deleted', custom_context)
    link_tasks(graph, 'Compute_uninstall', 'LinuxFileSystem-2_deleted', custom_context)
    link_tasks(graph, 'Compute_uninstall', 'LinuxFileSystem-3_deleted', custom_context)
    link_tasks(graph, 'Compute_uninstall', 'LinuxFileSystem-1_deleted', custom_context)
    link_tasks(graph, 'LinuxFileSystem-4_deleting', 'LinuxFileSystem-4_stopped', custom_context)
    link_tasks(graph, 'LinuxFileSystem-1_stopped', 'stop_LinuxFileSystem-1', custom_context)
    link_tasks(graph, 'LinuxFileSystem-4_stopped', 'stop_LinuxFileSystem-4', custom_context)
    link_tasks(graph, 'LinuxFileSystem-3_deleting', 'LinuxFileSystem-3_stopped', custom_context)
    link_tasks(graph, 'LinuxFileSystem-3_stopped', 'stop_LinuxFileSystem-3', custom_context)
    link_tasks(graph, 'LinuxFileSystem-4_deleted', 'LinuxFileSystem-4_deleting', custom_context)
    link_tasks(graph, 'LinuxFileSystem-2_deleted', 'LinuxFileSystem-2_deleting', custom_context)
    link_tasks(graph, 'LinuxFileSystem-2_deleting', 'LinuxFileSystem-2_stopped', custom_context)
    link_tasks(graph, 'CBS3_uninstall', 'LinuxFileSystem-3_deleted', custom_context)
    link_tasks(graph, 'CBS4_uninstall', 'LinuxFileSystem-4_deleted', custom_context)
    link_tasks(graph, 'LinuxFileSystem-1_deleted', 'LinuxFileSystem-1_deleting', custom_context)
    link_tasks(graph, 'stop_LinuxFileSystem-1', 'LinuxFileSystem-1_stopping', custom_context)
    link_tasks(graph, 'LinuxFileSystem-2_stopped', 'stop_LinuxFileSystem-2', custom_context)
    link_tasks(graph, 'stop_LinuxFileSystem-2', 'LinuxFileSystem-2_stopping', custom_context)
    link_tasks(graph, 'stop_LinuxFileSystem-3', 'LinuxFileSystem-3_stopping', custom_context)
    link_tasks(graph, 'stop_LinuxFileSystem-4', 'LinuxFileSystem-4_stopping', custom_context)
    link_tasks(graph, 'CBS2_uninstall', 'LinuxFileSystem-2_deleted', custom_context)


@workflow
def a4c_scale(ctx, node_id, delta, scale_compute, **kwargs):
    scaled_node = ctx.get_node(node_id)
    if not scaled_node:
        raise ValueError("Node {0} doesn't exist".format(node_id))
    if not is_host_node(scaled_node):
        raise ValueError("Node {0} is not a host. This workflow can only scale hosts".format(node_id))
    if delta == 0:
        ctx.logger.info('delta parameter is 0, so no scaling will take place.')
        return

    curr_num_instances = scaled_node.number_of_instances
    planned_num_instances = curr_num_instances + delta
    if planned_num_instances < 1:
        raise ValueError('Provided delta: {0} is illegal. current number of'
                         'instances of node {1} is {2}'
                         .format(delta, node_id, curr_num_instances))

    modification = ctx.deployment.start_modification({
        scaled_node.id: {
            'instances': planned_num_instances
        }
    })
    ctx.logger.info(
        'Deployment modification started. [modification_id={0} : {1}]'.format(modification.id, dir(modification)))
    try:
        if delta > 0:
            ctx.logger.info('Scaling host {0} adding {1} instances'.format(node_id, delta))
            added_and_related = _get_all_nodes(modification.added)
            added = _get_all_modified_node_instances(added_and_related, 'added')
            graph = ctx.graph_mode()
            ctx.internal.send_workflow_event(event_type='a4c_workflow_started',
                                             message=build_pre_event(WfStartEvent('scale', 'install')))
            custom_context = CustomContext(ctx, added, added_and_related)
            install_host(ctx, graph, custom_context, node_id)
            try:
                graph.execute()
            except:
                ctx.logger.error('Scale failed. Uninstalling node {0}'.format(node_id))
                graph = ctx.internal.task_graph
                for task in graph.tasks_iter():
                    graph.remove_task(task)
                try:
                    custom_context = CustomContext(ctx, added, added_and_related)
                    uninstall_host(ctx, graph, custom_context, node_id)
                    graph.execute()
                except:
                    ctx.logger.error('Node {0} uninstallation following scale failure has failed'.format(node_id))
                raise
        else:
            ctx.logger.info('Unscaling host {0} removing {1} instances'.format(node_id, delta))
            removed_and_related = _get_all_nodes(modification.removed)
            removed = _get_all_modified_node_instances(removed_and_related, 'removed')
            graph = ctx.graph_mode()
            ctx.internal.send_workflow_event(event_type='a4c_workflow_started',
                                             message=build_pre_event(WfStartEvent('scale', 'uninstall')))
            custom_context = CustomContext(ctx, removed, removed_and_related)
            uninstall_host(ctx, graph, custom_context, node_id)
            try:
                graph.execute()
            except:
                ctx.logger.error('Unscale failed.')
                raise
    except:
        ctx.logger.warn('Rolling back deployment modification. [modification_id={0}]'.format(modification.id))
        try:
            modification.rollback()
        except:
            ctx.logger.warn('Deployment modification rollback failed. The '
                            'deployment model is most likely in some corrupted'
                            ' state.'
                            '[modification_id={0}]'.format(modification.id))
            raise
        raise
    else:
        try:
            modification.finish()
        except:
            ctx.logger.warn('Deployment modification finish failed. The '
                            'deployment model is most likely in some corrupted'
                            ' state.'
                            '[modification_id={0}]'.format(modification.id))
            raise


@workflow
def a4c_heal(
        ctx,
        node_instance_id,
        diagnose_value='Not provided',
        **kwargs):
    """Reinstalls the whole subgraph of the system topology

    The subgraph consists of all the nodes that are hosted in the
    failing node's compute and the compute itself.
    Additionally it unlinks and establishes appropriate relationships

    :param ctx: cloudify context
    :param node_id: failing node's id
    :param diagnose_value: diagnosed reason of failure
    """

    ctx.logger.info("Starting 'heal' workflow on {0}, Diagnosis: {1}"
                    .format(node_instance_id, diagnose_value))
    failing_node = ctx.get_node_instance(node_instance_id)
    host_instance_id = failing_node._node_instance.host_id
    failing_node_host = ctx.get_node_instance(host_instance_id)
    node_id = failing_node_host.node_id
    subgraph_node_instances = failing_node_host.get_contained_subgraph()
    added_and_related = _get_all_nodes(ctx)
    try:
      graph = ctx.graph_mode()
      ctx.internal.send_workflow_event(event_type='a4c_workflow_started',
                                               message=build_pre_event(WfStartEvent('heal', 'uninstall')))
      custom_context = CustomContext(ctx, subgraph_node_instances, added_and_related)
      uninstall_host(ctx, graph, custom_context, node_id)
      graph.execute()
    except:
      ctx.logger.error('Uninstall while healing failed.')
    graph = ctx.internal.task_graph
    for task in graph.tasks_iter():
      graph.remove_task(task)
    ctx.internal.send_workflow_event(event_type='a4c_workflow_started',
                                             message=build_pre_event(WfStartEvent('heal', 'install')))
    custom_context = CustomContext(ctx, subgraph_node_instances, added_and_related)
    install_host(ctx, graph, custom_context, node_id)
    graph.execute()


#following code can be pasted in src/test/python/workflows/context.py for simulation
#def _build_nodes(ctx):
    #types = []
    #types.append('alien.nodes.LinuxFileSystem')
    #types.append('tosca.nodes.SoftwareComponent')
    #types.append('tosca.nodes.Root')
    #node_LinuxFileSystem-4 = _build_node(ctx, 'LinuxFileSystem-4', types, 1)
    #types = []
    #types.append('alien.nodes.LinuxFileSystem')
    #types.append('tosca.nodes.SoftwareComponent')
    #types.append('tosca.nodes.Root')
    #node_LinuxFileSystem-3 = _build_node(ctx, 'LinuxFileSystem-3', types, 1)
    #types = []
    #types.append('alien.nodes.LinuxFileSystem')
    #types.append('tosca.nodes.SoftwareComponent')
    #types.append('tosca.nodes.Root')
    #node_LinuxFileSystem-2 = _build_node(ctx, 'LinuxFileSystem-2', types, 1)
    #types = []
    #types.append('alien.nodes.LinuxFileSystem')
    #types.append('tosca.nodes.SoftwareComponent')
    #types.append('tosca.nodes.Root')
    #node_LinuxFileSystem-1 = _build_node(ctx, 'LinuxFileSystem-1', types, 1)
    #types = []
    #types.append('tosca.nodes.SoftwareComponent')
    #types.append('tosca.nodes.Root')
    #node__a4c_CBS1 = _build_node(ctx, '_a4c_CBS1', types, 1)
    #types = []
    #types.append('tosca.nodes.SoftwareComponent')
    #types.append('tosca.nodes.Root')
    #node__a4c_CBS3 = _build_node(ctx, '_a4c_CBS3', types, 1)
    #types = []
    #types.append('tosca.nodes.SoftwareComponent')
    #types.append('tosca.nodes.Root')
    #node__a4c_CBS2 = _build_node(ctx, '_a4c_CBS2', types, 1)
    #types = []
    #types.append('alien.nodes.openstack.ScalableCompute')
    #types.append('alien.nodes.openstack.Compute')
    #types.append('tosca.nodes.Compute')
    #types.append('tosca.nodes.Root')
    #node_Compute = _build_node(ctx, 'Compute', types, 1)
    #types = []
    #types.append('tosca.nodes.SoftwareComponent')
    #types.append('tosca.nodes.Root')
    #node__a4c_CBS4 = _build_node(ctx, '_a4c_CBS4', types, 1)
    #_add_relationship(node_LinuxFileSystem-4, node_Compute)
    #_add_relationship(node_LinuxFileSystem-4, node__a4c_CBS4)
    #_add_relationship(node_LinuxFileSystem-3, node__a4c_CBS3)
    #_add_relationship(node_LinuxFileSystem-3, node_Compute)
    #_add_relationship(node_LinuxFileSystem-2, node__a4c_CBS2)
    #_add_relationship(node_LinuxFileSystem-2, node_Compute)
    #_add_relationship(node_LinuxFileSystem-1, node__a4c_CBS1)
    #_add_relationship(node_LinuxFileSystem-1, node_Compute)
    #_add_relationship(node__a4c_CBS1, node_Compute)
    #_add_relationship(node__a4c_CBS3, node_Compute)
    #_add_relationship(node__a4c_CBS2, node_Compute)
    #_add_relationship(node__a4c_CBS4, node_Compute)
