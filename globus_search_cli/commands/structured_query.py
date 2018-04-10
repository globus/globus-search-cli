from __future__ import print_function

import json
import click

from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd, get_search_index


@globus_cmd('structured-query',
            help=('Perform a search based on an structured query document. '
                  'This document is sent verbatim to the Search API. May be '
                  'provided on stdin using "-"'))
@click.argument('query_document', type=click.File())
def structured_query_func(query_document):
    search_client = get_search_client()
    print(json.dumps(
        search_client.post_search(
            get_search_index(),
            json.load(query_document)).data,
        indent=2))
