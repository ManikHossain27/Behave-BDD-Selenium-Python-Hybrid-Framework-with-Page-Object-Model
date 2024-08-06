Feature: Register Account functionality

  Background:
    Given I navigate to Register page

  Scenario: Register with mandatory fields
    When I enter detaild into mandatory fields
    And I click on continue button
    Then Account should get created

  Scenario: Register with all fields
    When I enter details into all fields
    And I select Privacy Policy option
    And I click on continue button
    Then Account should get created

  Scenario: Register with duplicate email address
    When I enter details into all fields except email field
    And I enter existing accounts email into email field
    And I select Privacy Policy option
    And I click on continue button
    Then Proper warning message information about duplicate account should be displayed

 Scenario: Register without providing any details
    When I don't enter anything into the fields
    And I click on continue button
    Then Proper warning message for every mandatory fields should be displayed

