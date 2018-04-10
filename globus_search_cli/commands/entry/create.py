from __future__ import print_function

import json
import click

from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd, get_search_index


@globus_cmd('create', help='Create a single GMetaEntry')
@click.argument('source')
def create_func(source):
    search_client = get_search_client()
    with open(source) as f:
        print(json.dumps(
            search_client.create_entry(
                get_search_index(), f.read()).data,
            indent=2))
