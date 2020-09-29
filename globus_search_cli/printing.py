import json
import os
import sys

ENSURE_ASCII = os.getenv("GLOBUS_SEARCH_ENSURE_ASCII") == "1"


def safeprint(s):
    try:
        print(s)
        sys.stdout.flush()
    except IOError:
        pass


def format_output(dataobject):
    if isinstance(dataobject, str):
        safeprint(dataobject)
    else:
        safeprint(
            json.dumps(
                dataobject,
                indent=2,
                separators=(",", ": "),
                sort_keys=True,
                ensure_ascii=ENSURE_ASCII,
            )
        )
