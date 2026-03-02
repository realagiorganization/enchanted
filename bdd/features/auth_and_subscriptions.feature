Feature: Authentication and subscriptions
  As a user
  I want to sign in and manage my subscription
  So that I can access paid features with my preferred identity provider

  Scenario: Sign in with GitHub
    Given the app is installed
    When I choose GitHub login
    And I complete OAuth in the browser
    Then I am signed in with my GitHub account
    And my account screen shows GitHub as linked

  Scenario: Sign in with Discord
    Given the app is installed
    When I choose Discord login
    And I complete OAuth in the browser
    Then I am signed in with my Discord account
    And my account screen shows Discord as linked

  Scenario: Purchase a subscription via RevenueCat
    Given I am signed in
    And I see available plans
    When I purchase a plan
    Then the purchase succeeds
    And my entitlement status shows the new plan as active

  Scenario: Restore purchases on a new device
    Given I am signed in on a new device
    When I tap restore purchases
    Then my previous plan is restored
    And my entitlement status matches RevenueCat

  Scenario: Manage plan and cancellation
    Given I have an active plan
    When I open manage subscription
    And I choose to cancel at renewal
    Then my plan shows as set to cancel
    And I retain access until the current period ends
