"""
Config handling
Mostly cloned from globus-cli
"""


import os
import re

from globus_sdk_tokenstorage import SQLiteAdapter

import globus_sdk

from globus_search_cli import version
from globus_search_cli.server_timing import ServerTimingPrintMixin

__all__ = (
    "SEARCH_ALL_SCOPE",
    "SEARCH_RESOURCE_SERVER",
    "internal_auth_client",
    "get_search_client",
    "token_storage_adapter",
)

SEARCH_ALL_SCOPE = "urn:globus:auth:scope:search.api.globus.org:all"
SEARCH_RESOURCE_SERVER = "search.api.globus.org"


CLIENT_ID = "ee929f5c-ed08-4320-b22f-c1aa5229e490"


GLOBUS_ENV = os.environ.get("GLOBUS_SDK_ENVIRONMENT")
if GLOBUS_ENV:
    CLIENT_ID = {
        "sandbox": "f9e36a20-2e1a-49e5-ba67-34cc82ca8b29",
        "integration": "16ba55fb-5a93-4ee0-ae20-1a3a6cbb6c03",
        "test": "2aa543de-b6c6-4aa5-9d7b-ef28e3a28cd8",
        "staging": "0811fdd3-0d3e-4b5e-b634-8d6c91d87f21",
        "preview": "988ff3e0-3bcf-495a-9f12-3b3a309bdb36",
    }.get(GLOBUS_ENV, CLIENT_ID)

# explicitly set the base url with this var, e.g. set it to
# `localhost:8888` for development
BASE_URL = os.environ.get("GLOBUS_SEARCH_BASE_URL")
if BASE_URL is not None and not re.match("^https?://", BASE_URL):
    scheme = "http" if BASE_URL.startswith("localhost:") else "https"
    BASE_URL = scheme + "://" + BASE_URL


class SearchClient(ServerTimingPrintMixin, globus_sdk.SearchClient):
    pass


def internal_auth_client():
    return globus_sdk.NativeAppAuthClient(CLIENT_ID, app_name=version.app_name)


def token_storage_adapter():
    if not hasattr(token_storage_adapter, "_instance"):
        # namespace is equal to the current environment
        token_storage_adapter._instance = SQLiteAdapter(
            os.path.expanduser("~/.globus_search.db"), namespace=GLOBUS_ENV or "DEFAULT"
        )
    return token_storage_adapter._instance


def get_search_client():
    storage_adapter = token_storage_adapter()
    maybe_existing = storage_adapter.read_as_dict()

    refresh_token, access_token, access_token_expires = None, None, None
    if maybe_existing is not None and SEARCH_RESOURCE_SERVER in maybe_existing:
        searchdata = maybe_existing[SEARCH_RESOURCE_SERVER]
        access_token = searchdata["access_token"]
        refresh_token = searchdata["refresh_token"]
        access_token_expires = searchdata["expires_at_seconds"]

    authorizer = None
    if access_token_expires is not None:
        authorizer = globus_sdk.RefreshTokenAuthorizer(
            refresh_token,
            internal_auth_client(),
            access_token,
            int(access_token_expires),
            on_refresh=storage_adapter.on_refresh,
        )

    add_kwargs = {}
    if BASE_URL:
        add_kwargs["base_url"] = BASE_URL

    return SearchClient(
        authorizer=authorizer,
        app_name="search-client-cli v{}".format(version.__version__),
        **add_kwargs
    )
