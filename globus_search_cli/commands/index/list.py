from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd
from globus_search_cli.printing import format_output


@globus_cmd("list", help="List indices where you have some permissions")
def list_cmd():
    search_client = get_search_client()
    format_output(search_client.get("/v1/index_list").data)
