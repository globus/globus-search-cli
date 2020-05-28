import json
import sys


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
        safeprint(json.dumps(dataobject, indent=2, separators=(",", ": ")))
