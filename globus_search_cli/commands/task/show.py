import click

from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd
from globus_search_cli.printing import format_output


@globus_cmd("show", help="Display a Task")
@click.argument("task_id")
def show_cmd(task_id):
    search_client = get_search_client()
    format_output(search_client.get_task(task_id).data)
