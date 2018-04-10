from __future__ import print_function

import json
import copy
import click

from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd, get_search_index


@globus_cmd('ingest', help=('Send DOCUMENTS to Globus Search to index. '
                            'DOCUMENTS are paths to files, with "-" taken to '
                            'mean stdin'))
@click.option('--source-type', type=click.Choice(('gingest', 'gmetalist')),
              default='gingest', show_default=True,
              help=('How to consume each given document -- are they GIngest '
                    'documents to send verbatim to the service, or are they '
                    'GMetaLists which we will break into batches to send?'))
@click.option('--batch-size', type=int, default=100, show_default=True,
              help=('When source-type=GMetaList, how many entries to send '
                    'at a time'))
@click.argument('documents', nargs=-1, type=click.File())
def ingest_func(source_type, batch_size, documents):
    search_client = get_search_client()
    index = get_search_index()

    # limit batch size to the 1-1000 range
    batch_size = min(max(batch_size, 1), 1000)
    for document in documents:
        loaded_doc = json.load(document)
        if source_type == 'gingest':
            print(search_client.ingest(index, loaded_doc))
        elif source_type == 'gmetalist':
            entry_list = loaded_doc.pop('gmeta')
            current_doc = copy.copy(loaded_doc)
            while entry_list:
                current_slice = entry_list[:batch_size]
                entry_list = entry_list[batch_size:]

                current_doc['gmeta'] = current_slice
                gingest_doc = {
                    '@datatype': 'GIngest',
                    '@version': '2016-11-09',
                    'ingest_type': 'GMetaList',
                    'source_id': 'search_client_command',
                    'ingest_data': current_doc
                }
                print('Sending batch of size {}'.format(batch_size))
                print('-Start Results-')
                print(search_client.ingest(index, gingest_doc))
                print('-End Results-')
