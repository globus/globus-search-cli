from __future__ import print_function

import json
import click

from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd, get_search_index


@globus_cmd('delete', help='Remove all metadata about a subject')
@click.argument('subject')
def delete_func(subject):
    search_client = get_search_client()
    print(json.dumps(
        search_client.delete_subject(
            get_search_index(), subject).data))
