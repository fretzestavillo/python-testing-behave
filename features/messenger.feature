Feature: Automation in Messenger

  Scenario: Automation

    Given I launch Chrome browser
    When I open messenger
    And Enter credentials
    And clicklogin button
    And go to search bar and enter name of your friend
    And select specific friend
    And write message and send
    Then User must successfully login to homepage