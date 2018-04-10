from __future__ import print_function

import json
import click

from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd, get_search_index


@globus_cmd('show', help='Display a Query Template')
@click.argument('template_name')
def show_func(template_name):
    search_client = get_search_client()
    print(json.dumps(
        search_client.get_query_template(
            get_search_index(), template_name).data, indent=2))
