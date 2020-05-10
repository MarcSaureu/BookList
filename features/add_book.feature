Feature: Add Book
  In order to save a book for any reason,
  As a user,
  I want to create a book, with its details.

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Create a Book
    Given I login as user "user" with password "password"
    When I create a Book
      | ISBN         | title        | cover_page   | synopsis     | release_date | authors      |
      | 1234         | Book         | no_photo.png | Synopsis     | 03/12/1998   | Stephen, King|
    And There are 1 book
