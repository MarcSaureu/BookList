Feature: View Author
  In order to know about a author,
  As a user
  I want to view a author, with its details.

  Background: There is one author created by one user
    Given Exists a user "user1" with password "password"
    And Exists author by "user1"
      | firs_name    | last_name    | birth_date   | photo        |
      | firstname    | lastname     | 03/12/1998   | no_photo.png |
    And There are 1 author
