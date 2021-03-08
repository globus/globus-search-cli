import click

from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd, index_argument
from globus_search_cli.printing import format_output


@globus_cmd("query", help="Perform a search")
@click.option("--limit", type=int, help="Limit the number of results to return")
@click.option("--offset", type=int, help="Starting offset for paging")
@click.option(
    "--advanced",
    is_flag=True,
    help="Perform the search using the advanced query syntax",
)
@click.option(
    "--bypass-visible-to",
    is_flag=True,
    help="[admins only] Bypass the visible_to restriction on searches. "
    "This option is only available to the admins of an index",
)
# this option is in early development in Globus Search -- it may be dropped and is
# currently not documented (intentionally)
@click.option(
    "--filter-principal-sets",
    hidden=True,
)
@index_argument
@click.argument("query_string")
def query_func(
    index_id,
    query_string,
    limit,
    offset,
    bypass_visible_to,
    advanced,
    filter_principal_sets,
):
    search_client = get_search_client()
    format_output(
        search_client.search(
            index_id,
            query_string,
            advanced=advanced,
            bypass_visible_to=bypass_visible_to,
            limit=limit,
            offset=offset,
            filter_principal_sets=filter_principal_sets,
            result_format_version="2019-08-27",
        ).data
    )
