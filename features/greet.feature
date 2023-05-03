@rest @greet
Feature: Greet using base URL
  As a rest client user
  I want the service to say hello world to me
  So that I can be greeted

  @tier1
  Scenario: Get greeting
    When I call the greet endpoint
    Then I should get a greeting
