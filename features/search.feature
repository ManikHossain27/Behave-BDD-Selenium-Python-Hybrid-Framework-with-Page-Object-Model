Feature: Search functionality

  Background:
    Given I got navigated to Home page

  Scenario: Search for a valid product
    When I enter valid product into the Search box field
    And I click on Search button
    Then Valid product should get displayed in Search results

  Scenario: Search for an invalid product
    When I enter invalid product into the Search box field
    And I click on Search button
    Then Proper message should be displayed in Search results


  Scenario: Search without entering any product
    When I dont enter anything into Search box field
    And I click on Search button
    Then Proper message should be displayed in Search results