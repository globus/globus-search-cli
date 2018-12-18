import click

from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd
from globus_search_cli.printing import format_output


@globus_cmd("list", help="List the 1000 most recent Tasks for an index")
@click.argument("index_id")
def list_cmd(index_id):
    search_client = get_search_client()
    format_output(search_client.get_task_list(index_id).data)
