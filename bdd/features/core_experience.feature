Feature: Core Enchanted experience
  As a user
  I want to connect to my private model server and chat
  So that I can use Enchanted across my devices

  Scenario: Add a new server endpoint
    Given the app is installed
    When I open Settings
    And I enter a valid Ollama server URL
    Then the server endpoint is saved
    And the connection status shows as reachable

  Scenario: Start a new conversation
    Given a reachable server endpoint is configured
    When I create a new conversation
    And I send a prompt
    Then I see a streaming assistant response
    And the conversation appears in history

  Scenario: Use multimodal prompts
    Given a reachable server endpoint is configured
    When I attach an image to a prompt
    And I send the prompt
    Then the image is included with the request
    And the assistant responds with a multimodal answer

  Scenario: Use a system prompt template
    Given a system prompt template exists
    When I start a new conversation with that template
    Then the system prompt is applied to the conversation

Feature: Privacy and offline behavior
  As a user
  I want my data to stay on device
  So that my conversations remain private

  Scenario: Conversation history is stored locally
    Given I have active conversations
    When I close and reopen the app
    Then my conversation history is available on device
    And no cloud sync is required

  Scenario: Offline usage with local server
    Given the Ollama server is reachable on my network
    When I disable external network access
    And I send a prompt
    Then the request succeeds using the local server
    And the app remains functional offline
