from __future__ import print_function

import json
import click

from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd, get_search_index


@globus_cmd('show', help='Display all visible metadata about a Subject')
@click.argument('subject')
def show_func(subject):
    search_client = get_search_client()
    print(json.dumps(
        search_client.get_subject(
            get_search_index(), subject).data, indent=2))
