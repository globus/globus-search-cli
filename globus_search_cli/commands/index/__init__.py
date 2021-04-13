from globus_search_cli.commands.index.create import create_cmd
from globus_search_cli.commands.index.list import list_cmd
from globus_search_cli.commands.index.role import role_cmd
from globus_search_cli.commands.index.show import show_cmd
from globus_search_cli.parsing import globus_group


@globus_group("index", help="View and manage indices")
def index_cmd():
    pass


index_cmd.add_command(show_cmd)
index_cmd.add_command(list_cmd)
index_cmd.add_command(create_cmd)
index_cmd.add_command(role_cmd)
