import click

from globus_search_cli.config import get_search_client
from globus_search_cli.parsing import globus_cmd, index_argument
from globus_search_cli.printing import format_output


@globus_cmd("create", help="Create a role (requires admin or owner)")
@index_argument
@click.argument("ROLE_NAME")
@click.argument("PRINCIPAL")
@click.option(
    "--type",
    "principal_type",
    type=click.Choice(("identity", "group")),
    help=(
        "The type of the principal. "
        "If the principal is given as a URN, it will be checked against any provided "
        "'type'. If a non-URN string is given, the type will be used to format the "
        "principal as a URN."
    ),
)
def create_cmd(index_id, role_name, principal, principal_type):
    """
    Example usage:
       idx="...index ID here..."
       principal=ae341a98-d274-11e5-b888-dbae3a8ba545

       globus-search index role create writer $idx $principal --type identity
       globus-search index role create admin $idx "urn:globus:auth:identity:$principal"
    """
    if principal.startswith("urn:"):
        if principal_type == "identity" and not principal.startswith(
            "urn:globus:auth:identity:"
        ):
            raise click.UsageError(
                f"--type=identity but '{principal}' is not a valid identity URN"
            )
        if principal_type == "group" and not principal.startswith(
            "urn:globus:group:id:"
        ):
            raise click.UsageError(
                f"--type=group but '{principal}' is not a valid group URN"
            )
    else:
        if principal_type == "identity":
            principal = f"urn:globus:auth:identity:{principal}"
        elif principal_type == "group":
            principal = f"urn:globus:group:id:{principal}"
        else:
            raise click.UsageError(f"'{principal}' is not a valid URN")

    role_doc = {"role_name": role_name, "principal": principal}
    search_client = get_search_client()
    format_output(
        search_client.post(f"/v1/index/{index_id}/role", json_body=role_doc).data
    )
