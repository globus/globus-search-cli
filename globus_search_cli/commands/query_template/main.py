from globus_search_cli.parsing import globus_group
from globus_search_cli.commands.query_template.show import show_func
from globus_search_cli.commands.query_template.list import list_func


@globus_group('query-template', help="Display Query Templates")
def query_template_cmd():
    pass


query_template_cmd.add_command(show_func)
query_template_cmd.add_command(list_func)
