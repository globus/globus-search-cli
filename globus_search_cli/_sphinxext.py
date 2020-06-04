"""
This is a very simple sphinx extension which generates header lines for a changelog with
an (optional) label in parens, often used for a release date or alpha/beta description.

By default, the anchor links produced by sphinx for a simple changelog can be just
"id<N>" links, which aren't useful.

This plugin ensures that you have 'v' as a prefix (which makes the autogen anchors
better) and produces anchors with and without the label included. So you can refer to
`v0-4-0` even if the full link is `v0-4-0-beta`.
"""

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.statemachine import ViewList
from sphinx.util.nodes import nested_parse_with_titles

CL = "<changelog>"


class ChangelogEntry(Directive):
    has_content = False
    required_arguments = 1
    optional_arguments = 1

    def gen_rst(self):
        version = self.arguments[0]
        try:
            label = self.arguments[1]
        except IndexError:
            label = None

        yield ".. _v{}:".format(version)
        yield ""
        if label:
            yield ".. _v{}-{}:".format(version, label)
            yield ""

        headerline = version
        if label:
            headerline = "v{} ({})".format(version, label)
        yield headerline
        yield "-" * len(headerline)
        yield ""

    def run(self):
        viewlist = ViewList()
        for line in self.gen_rst():
            print(line)
            viewlist.append(line, CL)
        node = nodes.section()
        node.document = self.state.document
        nested_parse_with_titles(self.state, viewlist, node)
        return node.children


def setup(app):
    app.add_directive("changelog", ChangelogEntry)
