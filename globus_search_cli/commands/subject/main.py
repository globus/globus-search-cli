from globus_search_cli.commands.subject.delete import delete_func
from globus_search_cli.commands.subject.show import show_func
from globus_search_cli.parsing import globus_group


@globus_group("subject", help="View and delete Subjects and their contents")
def subject_cmd():
    pass


subject_cmd.add_command(show_func)
subject_cmd.add_command(delete_func)
