Feature: Add Book
  In order to save a book in my registered list for any reason,
  As a user,
  I want add a book in the corresponding list, with its details.

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Add a book to a list
    Given I login as user "user" with password "password"
    When I add a book to a list
      | name      |
      | Book      |
    Then I'm viewing the details page for book by "user"
      | name      |
      | Book      |
    And There are 1 book
