Feature: Edit List
  In order to keep updated my previous registers about lists,
  As a user
  I want to edit a list I created.

  Background: There are registered users and a list by one of them
      Given Exists a user "user1" with password "password"
      And Exists a user "user2" with password "password"
      And Exists list registered by "user1"
        | name            |
        | Booklist1       |
    Scenario: Edit owned list name
      Given I login as user "user1" with password "password"
      When I edit the list with name "Booklist1"
        | name            |
        | BooklistEdited1 |
      And There are 1 list
