from __future__ import print_function

import json
import click

from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd, get_search_index


@globus_cmd('delete', help='Remove a specific entry')
@click.option('--entry-id', help='ID for the specific entry (null if absent)')
@click.argument('subject')
def delete_func(subject, entry_id):
    search_client = get_search_client()
    print(json.dumps(
        search_client.delete_entry(
            get_search_index(), subject, entry_id=entry_id).data,
        indent=2))
