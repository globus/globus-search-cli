from globus_search_cli.commands.index.role.create import create_cmd
from globus_search_cli.commands.index.role.delete import delete_cmd
from globus_search_cli.commands.index.role.list import list_cmd
from globus_search_cli.parsing import globus_group


@globus_group("role", help="View and manage index roles")
def role_cmd():
    pass


role_cmd.add_command(list_cmd)
role_cmd.add_command(delete_cmd)
role_cmd.add_command(create_cmd)
