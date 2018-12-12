from globus_search_cli.parsing.click_wrappers import globus_group


def main_func(f):
    """
    Wrap root command func in common opts and make it a command group
    """
    f = globus_group("search-client", help="CLI Client to the Globus Search API")(f)
    return f
