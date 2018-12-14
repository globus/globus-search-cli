from globus_search_cli.commands import (
    entry_cmd,
    ingest_func,
    login_command,
    logout_command,
    query_func,
    query_template_cmd,
    show_index_cmd,
    structured_query_func,
    subject_cmd,
    task_cmd,
)
from globus_search_cli.parsing import main_func


@main_func
def cli_root():
    pass


cli_root.add_command(show_index_cmd)
cli_root.add_command(ingest_func)
cli_root.add_command(query_func)
cli_root.add_command(structured_query_func)
cli_root.add_command(subject_cmd)
cli_root.add_command(entry_cmd)
cli_root.add_command(task_cmd)
cli_root.add_command(query_template_cmd)
cli_root.add_command(login_command)
cli_root.add_command(logout_command)
