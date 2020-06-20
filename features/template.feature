@basic
Feature: Template requirements
  As a regular user,
  I want to ensure the template has 100% coverage.

  @version
  Scenario: Run template functions
    Given template.py exists
    Then run all the functions to test coverage
