Feature: Add Author
  In order to save a author for any reason,
  As a user,
  I want to create a author, with its details.

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Create a Author
    Given I login as user "user" with password "password"
    When I create a Author
      | firs_name    | last_name    | birth_date   | photo        |
      | firstname    | lastname     | 03/12/1998   | no_photo.png |
    And There are 1 author
