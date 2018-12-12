from globus_search_cli.commands.entry.create import create_func
from globus_search_cli.commands.entry.delete import delete_func
from globus_search_cli.commands.entry.show import show_func
from globus_search_cli.commands.entry.update import update_func
from globus_search_cli.parsing import globus_group


@globus_group("entry", help="Modify and view GMetaEntry documents")
def entry_cmd():
    pass


entry_cmd.add_command(show_func)
entry_cmd.add_command(delete_func)
entry_cmd.add_command(create_func)
entry_cmd.add_command(update_func)
