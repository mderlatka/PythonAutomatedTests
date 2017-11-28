Feature: Test navigation between pages
  Scenario: Homepage can go to Teach Online page
    Given I am on the home page with "english" language set
    When I click on the 'Teach on Udemy' element
    Then I should be on the Teach Online page

  Scenario: Teach Online page can go to Homepage
    Given I am on the Teach Online page with "english" language set
    When I click on the 'logo site' element
    Then I should be on the home page