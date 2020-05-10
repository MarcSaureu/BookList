Feature: Edit Author
  In order to keep updated my previous registers about authors,
  As a user
  I want to edit a author I created.

  Background: There are registered users and a author
      Given Exists a user "user1" with password "password"
      And Exists a user "user2" with password "password"
      And Exists author registered by "user1"
        | name            |
        | Author1         |
    Scenario: Edit owned author name
      Given I login as user "user1" with password "password"
      When I edit the author with name "Author1"
        | name            |
        | AuthorEdited1 |
      And There are 1 author
