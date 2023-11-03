Feature: API Comparison

Scenario: Comparing two equal API responses
  Given I have API request URLs from "file1.txt" and "file2.txt"
  When I compare the API responses
  Then the responses should be equal

Scenario: Comparing two different API responses
  Given I have API request URLs from "file1.txt" and "file2.txt"
  When I compare the API responses
  Then the responses should not be equal
