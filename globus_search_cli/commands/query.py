import click

from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd, index_argument
from globus_search_cli.printing import format_output


@globus_cmd("query", help="Perform a search")
@click.option(
    "--query-template",
    help=(
        "A predefined Query Template name in the search service. "
        "Correct usage relies on prior knowledge of valid names"
    ),
)
@click.option("--limit", type=int, help="Limit the number of results to return")
@click.option("--offset", type=int, help="Starting offset for paging")
@index_argument
@click.argument("query_string")
def query_func(index_id, query_string, query_template, limit, offset):
    search_client = get_search_client()
    format_output(
        search_client.search(
            index_id,
            query_string,
            query_template=query_template,
            limit=limit,
            offset=offset,
        ).data
    )
