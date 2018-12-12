import copy
import json

import click

from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd, index_argument
from globus_search_cli.printing import format_output


@globus_cmd(
    "ingest",
    help=(
        "Send DOCUMENTS to Globus Search to index. "
        'DOCUMENTS are paths to files, with "-" taken to '
        "mean stdin"
    ),
)
@click.option(
    "--source-type",
    type=click.Choice(("gingest", "gmetalist")),
    default="gingest",
    show_default=True,
    help=(
        "How to consume each given document -- are they GIngest "
        "documents to send verbatim to the service, or are they "
        "GMetaLists which we will break into batches to send?"
    ),
)
@click.option(
    "--batch-size",
    type=int,
    default=100,
    show_default=True,
    help=("When source-type=GMetaList, how many entries to send " "at a time"),
)
@index_argument
@click.argument("documents", nargs=-1, type=click.File())
def ingest_func(index_id, source_type, batch_size, documents):
    search_client = get_search_client()

    # limit batch size to the 1-1000 range
    batch_size = min(max(batch_size, 1), 1000)
    for document in documents:
        loaded_doc = json.load(document)
        if source_type == "gingest":
            format_output(search_client.ingest(index_id, loaded_doc).data)
        elif source_type == "gmetalist":
            entry_list = loaded_doc.pop("gmeta")
            current_doc = copy.copy(loaded_doc)
            while entry_list:
                current_slice = entry_list[:batch_size]
                entry_list = entry_list[batch_size:]

                current_doc["gmeta"] = current_slice
                gingest_doc = {
                    "@datatype": "GIngest",
                    "@version": "2016-11-09",
                    "ingest_type": "GMetaList",
                    "source_id": "search_client_command",
                    "ingest_data": current_doc,
                }
                format_output("Sending batch of size {}".format(batch_size))
                format_output("-Start Results-")
                format_output(search_client.ingest(index_id, gingest_doc).data)
                format_output("-End Results-")
