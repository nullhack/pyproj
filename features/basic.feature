@basic
Feature: Basic requirements
  As a developer,
  I want to show off my awesome project,
  So other users can use It too.

  @version
  Scenario Outline: Check Cli
    Given Main module exists
    When the argument `--show` is "<value>"
    Then "<output>" is shown

    Examples:
      | value | output       |
      | True  | hello world  |
      | False | *****        |
