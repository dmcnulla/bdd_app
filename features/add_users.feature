@rest @tier2
Feature: Add Users
  As an admin
  I want to add users
  so those users can use the system

  @add_user
  Scenario: Add new user
      Given I have no users
      When I add a new user "elvis" with password "presley"
      Then user "elvis" is in the system
      And user "elvis" has a password of "presley"

  @add_user
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

  @check_user
  Scenario: Existing user can be retrieved
    Given I have a user "elvis" with password "presley"
    When I retrieve the user "elvis"
    Then the user's password is "presley"

  @check_users
  Scenario: Existing users can be retrieved
    Given I only have the following users:
      | username | password |
      | elvis    | presley  |
      | john     | doe      |
      | jane     | doe      |
    When I retrieve all users
    Then the retrieved users are:
      | username | password |
      | elvis    | presley  |
      | john     | doe      |
      | jane     | doe      |

  @check_user
  Scenario: No password
    Given I have a user 'elvis'
    But the user has no password
    When I retrieve the user 'elvis'
    Then the user's password is empty
