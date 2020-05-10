Feature: Edit Book
  In order to keep updated my previous registers about books,
  As a user
  I want to edit a book I created.

  Background: There are registered users and books
      Given Exists a user "user1" with password "password"
      And Exists a user "user2" with password "password"
      And Exists book registered by "user1"
        | name            |
        | Book1           |
    Scenario: Edit owned book name
      Given I login as user "user1" with password "password"
      When I edit the book with name "Book1"
        | name            |
        | BookEdited1 |
      And There are 1 book
