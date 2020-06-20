"""This module contains step definitions for template.feature.

It uses the default 'parse' for step parameters:
http://behave.readthedocs.io/en/latest/tutorial.html#step-parameters
"""

import logging

from behave import given, then

logger = logging.Logger(__name__)


@given("template.py exists")
def step_impl(context):
    from python_project_template import template


@then("run all the functions to test coverage")
def step_impl(context):
    from python_project_template import template as t

    t.function_with_types_in_docstring("param1", "param2")
    t.function_with_pep484_type_annotations(1, 2)
    t.module_level_function("param1", param2="param2")
    try:
        t.module_level_function("param1", param2="param1")
    except ValueError as err:
        logger.warning(err)
    gen = t.example_generator(5)
    logger.info([i for i in gen])
    try:
        t.ExampleError("msg", 1)
    except Exception as err:
        logger.warning(err)
    c =t.ExampleClass("param1", "param2", "param3")
    c.readonly_property
    c.readwrite_property
    c.readwrite_property = 1
    c.example_method("param1", "param2")
    c.__special__()
    c.__special_without_docstring__()
    c._private()
    c._private_without_docstring()
