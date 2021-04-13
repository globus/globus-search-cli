import click

from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd
from globus_search_cli.printing import format_output


@globus_cmd("create", help="Create a new Index (beta)")
@click.argument("DISPLAY_NAME")
@click.argument("DESCRIPTION")
def create_cmd(display_name, description):
    index_doc = {"display_name": display_name, "description": description}
    search_client = get_search_client()
    format_output(search_client.post("/beta/index", json_body=index_doc).data)
