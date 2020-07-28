"""
Parse and display Server-Timing header info

Provides a mixin which lets you tweak existing globus-sdk client classes to
have this behavior on all responses.
The mixin is toggled by an environment variable
"""
import os
import shutil
import sys

GREEN = "0;32"
YELLOW = "0;33"
GRAY = "0;37"

# the amount to adjust spacing for ansi colorized strings
ANSI_OFFSET = 11


def _ansi(text, color):
    return "\033[{}m{}\033[0m".format(color, text)


def timing_string_to_dict(server_timing_string):
    """
    Given a Server Timing value as a string, parse it into a dict of the format
      nice_name: value

    For example

      'a=1, "alpha"; b=2'

    will parse as

      {"alpha": 1, "b": 2}

    """

    def parse_item(item):
        item = [x.strip() for x in item.split(";")]
        assert len(item) <= 2, "Too many semicolons in timing item, cannot parse"
        nice_name = None
        if len(item) == 2:
            nice_name = item[1].strip('"')
            item = item[0]
        item = item.split("=")
        assert len(item) == 2, "Wrong number of '=' delimited values"
        if not nice_name:
            nice_name = item[0]
        return (nice_name, float(item[1]))

    items = [x.strip() for x in server_timing_string.split(",")]
    return {key: value for (key, value) in [parse_item(x) for x in items]}


def render_dict_onscreen(timing_dict):
    print(_ansi("Server Timing Info", GREEN), file=sys.stderr)
    term_width = shutil.get_terminal_size((80, 20)).columns
    use_width = term_width - 4

    items = sorted(list(timing_dict.items()), key=lambda x: x[1])
    items = [("{}={}".format(*item), item[1]) for item in items]
    last = items[-1]
    factor = last[1]
    desc_width = (max(len(x[0]) for x in items) if items else 0) + 1

    print(_ansi("+" + "-" * (term_width - 2) + "+", GRAY), file=sys.stderr)
    for desc, size in items:
        desc = desc.ljust(desc_width, ".")
        bar_width = max(int((use_width - desc_width) * size / factor), 1)
        bar = "#" * bar_width
        msg = (desc + _ansi(bar, YELLOW)).ljust(use_width + ANSI_OFFSET, " ")
        print("{bar} {} {bar}".format(msg, bar=_ansi("|", GRAY)), file=sys.stderr)
    print(_ansi("+" + "-" * (term_width - 2) + "+", GRAY), file=sys.stderr)


def render_timing_from_response(response):
    if os.getenv("SHOW_SERVER_TIMING") != "1":
        return
    timing_str = response._data.headers.get("Server-Timing")
    if timing_str:
        render_dict_onscreen(timing_string_to_dict(timing_str))


class ServerTimingPrintMixin:
    def _request(self, *args, **kwargs):
        try:
            response = super()._request(*args, **kwargs)
            render_timing_from_response(response)
            return response
        # if a "normal" API error occurred, there may be timing info
        except self.error_class as e:
            try:
                response = e._underlying_response
                render_timing_from_response(response)
            except Exception:
                pass
            raise e from e
