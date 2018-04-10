from __future__ import print_function

import json

from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd, get_search_index


@globus_cmd('list', help='List all query templates for an index')
def list_func():
    search_client = get_search_client()
    print(json.dumps(
        search_client.list_query_templates(
            get_search_index()
        ).data, indent=2))
