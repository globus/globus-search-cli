from __future__ import print_function

import json
import click

from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd, get_search_index


@globus_cmd('query', help='Perform a search')
@click.option('--query-template',
              help=('A predefined Query Template name in the search service. '
                    'Correct usage relies on prior knowledge of valid names'))
@click.option('--limit', type=int,
              help='Limit the number of results to return')
@click.option('--offset', type=int, help='Starting offset for paging')
@click.argument('query_string')
def query_func(query_string, query_template, limit, offset):
    search_client = get_search_client()
    print(
        json.dumps(
            search_client.search(
                get_search_index(), query_string,
                query_template=query_template,
                limit=limit,
                offset=offset).data,
            indent=2)
        )
