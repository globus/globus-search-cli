from globus_search_cli.parsing import main_func
from globus_search_cli.commands import (
    ingest_func, query_func, structured_query_func,
    subject_cmd, entry_cmd, query_template_cmd,
    login_command, logout_command)


@main_func
def cli_root():
    pass


cli_root.add_command(ingest_func)
cli_root.add_command(query_func)
cli_root.add_command(structured_query_func)
cli_root.add_command(subject_cmd)
cli_root.add_command(entry_cmd)
cli_root.add_command(query_template_cmd)
cli_root.add_command(login_command)
cli_root.add_command(logout_command)
