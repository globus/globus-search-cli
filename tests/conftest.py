import os
import shlex

import click
import pytest
import responses
from click.testing import CliRunner

from globus_search_cli import cli_root


@pytest.fixture(autouse=True)
def mocked_responses(monkeypatch):
    """
    All tests enable `responses` patching of the `requests` package, replacing
    all HTTP calls.
    """
    responses.start()

    # while request mocking is running, ensure GLOBUS_SDK_ENVIRONMENT is set to
    # production
    monkeypatch.setitem(os.environ, "GLOBUS_SDK_ENVIRONMENT", "production")

    yield

    responses.stop()
    responses.reset()


@pytest.fixture
def run_line(monkeypatch):
    """
    a simplified CLIRunner interface for most of our testing
    """

    def _run_line(
        line, assert_exit_code=0, disable_custom_excepthook=True, unstyle=True
    ):
        """
        Uses click.testing's CliRunner to run the given command line.

        Asserts that the exit_code is equal to the given assert_exit_code,
        and if that exit_code is 0 prevents click from catching exceptions
        for easier debugging.

        By default, disables the custom excepthook used to parse and display errors.
        This makes it much easier to tell where/why a test is failing.
        If a test is checking that error handling, pass
        'disable_custom_excepthook=False'

        When unstyle=True (default), any ANSI styling will be stripped from output

        Returns the output of running the line.
        """

        if disable_custom_excepthook:
            monkeypatch.setattr(
                cli_root, "invoke", lambda ctx: click.Group.invoke(cli_root, ctx)
            )

        # split line into args and confirm line starts with "globus-search"
        args = shlex.split(line)
        assert args[0] == "globus-search"

        # run the line. cli_root is the "globus-search-cli" command
        # if we are expecting success (0), don't catch any exceptions.
        result = CliRunner().invoke(
            cli_root, args[1:], catch_exceptions=bool(assert_exit_code)
        )
        # confirm expected exit_code
        if result.exit_code != assert_exit_code:
            raise (
                Exception(
                    (
                        "CliTest run_line exit_code assertion failed!\n"
                        "Line:\n{}\nexited with {} when expecting {}\n"
                        "Output:\n{}".format(
                            line, result.exit_code, assert_exit_code, result.output
                        )
                    )
                )
            )
        # fetch and optionally strip ANSI styling from output
        output = result.output
        if unstyle:
            output = click.unstyle(output)
        # return the output for further testing
        return output

    return _run_line
