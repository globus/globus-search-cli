import click

from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd, index_argument
from globus_search_cli.printing import format_output


@globus_cmd("delete", help="Delete a role (requires admin or owner)")
@index_argument
@click.argument("ROLE_ID")
def delete_cmd(index_id, role_id):
    search_client = get_search_client()
    format_output(search_client.delete(f"/v1/index/{index_id}/role/{role_id}").data)
