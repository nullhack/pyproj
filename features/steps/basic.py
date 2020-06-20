"""This module contains step definitions for basic.feature.

It uses the default 'parse' for step parameters:
http://behave.readthedocs.io/en/latest/tutorial.html#step-parameters
"""

import sys
from io import StringIO

from behave import given, then, when


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio  # free up some memory
        sys.stdout = self._stdout


# Givens


@given("Main module exists")
def step_impl(context):
    import cli

    context.cli = cli


# Whens


@when('the argument `--show` is "{value}"')
def step_impl(context, value):
    context.cli_value = True if str(value).lower() == "true" else False


# Thens


@then('"{output}" is shown')
def step_impl(context, output):
    with Capturing() as stdout:
        context.cli.run(show=context.cli_value)
    assert output == stdout[0]
