import click

from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd, index_argument
from globus_search_cli.printing import format_output


@globus_cmd("delete", help="Remove a specific entry")
@click.option("--entry-id", help="ID for the specific entry (null if absent)")
@index_argument
@click.argument("subject")
def delete_func(index_id, subject, entry_id):
    search_client = get_search_client()
    format_output(search_client.delete_entry(index_id, subject, entry_id=entry_id).data)
