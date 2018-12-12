import click

from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd, index_argument
from globus_search_cli.printing import format_output


@globus_cmd("show", help="Display all visible metadata about a Subject")
@index_argument
@click.argument("subject")
def show_func(index_id, subject):
    search_client = get_search_client()
    format_output(search_client.get_subject(index_id, subject).data)
