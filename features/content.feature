# -*- coding: utf-8 -*-

Feature: Veryfying the elements on the Udemy.com home page are visible

  Scenario: The Udemy home site should have correct title
    Given I am on the home page with "english" language set
    Then The title is shown on the page
    And the page title should be "Online Courses - Learn Anything, On Your Schedule | Udemy"

  Scenario: The Udemy home page should have correct url
    Given I am on the home page with "english" language set
    Then current url should be "www.udemy.com"

  Scenario: Verify the footer, its sections are visible
    Given I am on the home page with "english" language set
    Then Footer should be visible
    And "upper footer" section should be on page
    And "bottom footer" section should be on page

  Scenario: Verfify the navigation bar and its elements on home page are visible
    Given I am on the home page with "english" language set
    Then main navigation bar should be visible
    And on this bar "logo site" element should be visible
    And on this bar "categories" element should be visible
    And on this bar "search for courses form" element should be visible
    And on this bar "Udemy for business" element should be visible
    And on this bar "Cart icon" element should be visible
    And on this bar "Log in" element should be visible
    And on this bar "Sign up" element should be visible
    And on this bar "Teach on Udemy" element should be visible