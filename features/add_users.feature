@rest
Feature: Add Users
  As an admin
  I want to add users
  so those users can use the system

  Scenario: Add new user
      Given I have no users
      When I add a new user "elvis" with password "presley"
      Then user "elvis" is in the system
      And user "elvis" has a password of "presley"

  Scenario Outline: Add new users
      Given I have no users
      When I add a new user "<username>" with password "<password>"
      Then user "<username>" is in the system
      And user "<username>" has a password of "<password>"
    Examples:
      | username | password |
      | elvis    | presley  |
      | john     | doe      |
      | jane     | doe      |
