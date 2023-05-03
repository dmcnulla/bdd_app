@rest
@update_user
Feature: Update Users
  As an admin
  I want to update users
  so they can have new passwords

  @wip
  Scenario: Update user's password
    Given I have a user "elvis" with password "presley"
    When I update the user "elvis" to change password "presley" to "presley2"
    And I retrieve the user "elvis"
    Then the user's password is "presley2"
