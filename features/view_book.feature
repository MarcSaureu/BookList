Feature: View Book
  In order to know about a book,
  As a user
  I want to view a book, with its details.

  Background: There is one book created by one user
    Given Exists a user "user1" with password "password"
    And Exists book by "user1"
      | ISBN         | title        | cover_page   | synopsis     | release_date | authors      |
      | 1234         | Book         | no_photo.png | Synopsis     | 03/12/1998   | Stephen, King|
    And There are 1 book
