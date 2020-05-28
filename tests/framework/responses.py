"""copied mostly from gcs-cli test fixture config"""
import json
import os

import httpretty
import yaml

from globus_sdk.base import slash_join

_base_url_map = {
    "search": "https://search.api.globus.org/",
    "auth": "https://auth.globus.org/",
}

_response_fixtures = {}


def get_response_fixtures(service):
    global _response_fixtures

    if service in _response_fixtures:
        return _response_fixtures[service]

    file_path = os.path.dirname(__file__) + "/{}_response_fixtures.yaml".format(service)

    with open(file_path, "r") as stream:
        _response_fixtures[service] = yaml.safe_load(stream)

    return _response_fixtures[service]


def get_fixture_example_response_body(service, path, method, example_name):
    spec = get_response_fixtures(service)
    data = spec["paths"][path][method]["examples"][example_name]
    return json.dumps(data).encode("utf8")


def register_api_route_from_fixtures(
    service, path, method, code, example_name="default", **kwargs
):
    """
    Handy wrapper for adding URIs to the HTTPretty state from the
    response_fixtures
    """
    register_api_route_from_string(
        service,
        path,
        method,
        code,
        get_fixture_example_response_body(service, path, method.lower(), example_name),
        **kwargs
    )


def register_api_route_from_string(
    service, path, method, code, payload_string, adding_headers=None, **kwargs
):
    """
    Handy wrapper for adding URIs to the HTTPretty state.
    """
    assert httpretty.is_enabled()
    assert service in _base_url_map
    base_url = _base_url_map.get(service)
    full_url = slash_join(base_url, path)

    # can set it to `{}` explicitly to clear the default
    if adding_headers is None:
        adding_headers = {"Content-Type": "application/json"}

    httpretty.register_uri(
        method,
        full_url,
        status=code,
        body=payload_string,
        adding_headers=adding_headers,
        **kwargs
    )
