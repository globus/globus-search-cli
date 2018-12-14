from globus_search_cli.commands.task.list import list_cmd
from globus_search_cli.commands.task.show import show_cmd
from globus_search_cli.parsing import globus_group


@globus_group("task", help="Modify and view Task documents")
def task_cmd():
    pass


task_cmd.add_command(show_cmd)
task_cmd.add_command(list_cmd)
