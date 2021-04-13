from globus_search_cli.commands.delete_by_query import delete_by_query_cmd
from globus_search_cli.commands.entry import entry_cmd
from globus_search_cli.commands.index import index_cmd
from globus_search_cli.commands.ingest import ingest_func
from globus_search_cli.commands.login import login_command
from globus_search_cli.commands.logout import logout_command
from globus_search_cli.commands.query import query_func
from globus_search_cli.commands.structured_query import structured_query_func
from globus_search_cli.commands.subject import subject_cmd
from globus_search_cli.commands.task import task_cmd
from globus_search_cli.parsing import main_func


@main_func
def cli_root():
    pass


cli_root.add_command(index_cmd)
cli_root.add_command(ingest_func)
cli_root.add_command(query_func)
cli_root.add_command(structured_query_func)
cli_root.add_command(delete_by_query_cmd)
cli_root.add_command(subject_cmd)
cli_root.add_command(entry_cmd)
cli_root.add_command(task_cmd)
cli_root.add_command(login_command)
cli_root.add_command(logout_command)
