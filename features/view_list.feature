Feature: View List
  In order to know about a list,
  As a user
  I want to view a list, with its books and details.

  Background: There is one list with one book
    Given Exists a user "user1" with password "password"
    And Exists list registered by "user1"
      | name         |
      | BookList1    |
    And Exists book at list "BookList1" by "user1"
      | ISBN         | title        | cover_page   | synopsis     | release_date | authors      |
      | 1234         | Book         | no_photo.png | Synopsis     | 03/12/1998   | Stephen, King|
    And There are 1 list
    And There are 1 book
