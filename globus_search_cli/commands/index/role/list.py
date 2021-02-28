from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd, index_argument
from globus_search_cli.printing import format_output


@globus_cmd("list", help="List roles on an index (requires admin)")
@index_argument
def list_cmd(index_id):
    search_client = get_search_client()
    format_output(search_client.get(f"/v1/index/{index_id}/role_list").data)
