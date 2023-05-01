@rest @greet
Feature: Greet using base URL
  As a rest client
  I want the service to say hello world to me
  So that I can be greeted

  Scenario: Greet
    Given I have a user rest service
    When I call the greet endpoint
    Then I should get a greeting
