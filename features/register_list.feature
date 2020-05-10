Feature: Register List
  In order to keep track of books I want to read or I have read,
  As a user,
  I want to register a list with its name and description.

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register just list name
    Given I login as user "user" with password "password"
    When I register List
      | name      |
      | Book List |
    And There are 1 list
