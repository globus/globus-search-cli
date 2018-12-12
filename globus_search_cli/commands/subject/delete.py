import click

from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd, index_argument
from globus_search_cli.printing import format_output


@globus_cmd("delete", help="Remove all metadata about a subject")
@index_argument
@click.argument("subject")
def delete_func(index_id, subject):
    search_client = get_search_client()
    format_output(search_client.delete_subject(index_id, subject).data)
