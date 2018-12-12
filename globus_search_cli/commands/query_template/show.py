import click

from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd, index_argument
from globus_search_cli.printing import format_output


@globus_cmd("show", help="Display a Query Template")
@index_argument
@click.argument("template_name")
def show_func(index_id, template_name):
    search_client = get_search_client()
    format_output(search_client.get_query_template(index_id, template_name).data)
