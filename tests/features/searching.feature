# Created by kevinmezui at 4/1/21
@web @google

Feature: Google Web Browsing
  As a web user,
  I want to find information online,
  In order to learn new things and put them into practice.

  Scenario: Basic Google Search
    Given the Google home page is displayed
    When the user searches for "python"
    Then results are shown for "python"
