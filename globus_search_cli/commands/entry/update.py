import click

from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd, index_argument
from globus_search_cli.printing import format_output


@globus_cmd("update", help="Update a single GMetaEntry")
@index_argument
@click.argument("source")
def update_func(index_id, source):
    search_client = get_search_client()
    with open(source) as f:
        format_output(search_client.update_entry(index_id, f.read()).data)
