from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd, index_argument
from globus_search_cli.printing import format_output


@globus_cmd("show-index", help="Display information about an index")
@index_argument
def show_index_cmd(index_id):
    search_client = get_search_client()
    format_output(search_client.get_index(index_id).data)
