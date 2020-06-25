"""This module contains step definitions for template.feature.

It uses the default 'parse' for step parameters:
http://behave.readthedocs.io/en/latest/tutorial.html#step-parameters
"""

import logging

from behave import given, then

logger = logging.Logger(__name__)


@given("template.py exists")
def step_impl(context):
    from pyproj import template

    assert template.__name__


@then("run all the functions to test coverage")
def step_impl(context):
    from pyproj import template as t

    assert t.template_function("hello") == "hello"
    assert t.template_function("world", False) == ""
    c = t.TemplateClass("hello")
    assert c.message == "hello"
    c = t.TemplateClass("hello", False)
    assert c.message == ""
