import click

from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd, index_argument
from globus_search_cli.printing import format_output


@globus_cmd("delete-by-query", help="Perform a delete-by-query")
@click.option(
    "--advanced",
    is_flag=True,
    help="Perform the search using the advanced query syntax",
)
@index_argument
@click.argument("query_string")
def delete_by_query_cmd(index_id, query_string, advanced):
    search_client = get_search_client()
    format_output(
        search_client.delete_by_query(
            index_id,
            {
                "q": query_string,
                "advanced": advanced,
            },
        ).data
    )
