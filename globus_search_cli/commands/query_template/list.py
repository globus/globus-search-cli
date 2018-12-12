from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd, index_argument
from globus_search_cli.printing import format_output


@globus_cmd("list", help="List all query templates for an index")
@index_argument
def list_func(index_id):
    search_client = get_search_client()
    format_output(search_client.get_query_template_list(index_id).data)
