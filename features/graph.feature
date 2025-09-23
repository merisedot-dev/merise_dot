Feature: MCD root graph handling.

    Scenario: New graph creation.
        Given the graph currently does not exist
        When we create a new graph named "test_g"
        Then the graph exists
        And the graph name is "test_g"
        And the graph has 0 entities
        And the graph has 0 links

    Scenario Outline: New entity in graph
        Given a graph named "test"
        And the graph has 0 entities
        When we add an entity named "<name>"
        Then the graph has 1 entity

        Examples:
            |name      |
            |test_e    |
            |miaouh    |
            |jean-eudes|
            |123456    |
            |1test42   |

    Scenario Outline: Fetch entity by name
        Given a graph named "test"
        And an entity named "<name>" in graph
        When we fetch the "<name>" entity
        Then an entity is returned
        And the name of the entity is "<name>"

        Examples:
            |name |
            |kitty|
            |12345|
            |j    |

    Scenario Outline: Deleting entity from graph
        Given a graph named "test"
        And the graph has <ns> entities
        When we delete an entity from graph
        Then the graph has <nd> entities

        Examples:
            |ns|nd|
            |1 |0 |
            |25|24|

    Scenario: Deleting entity from empty graph
        Given a graph named "test"
        And the graph has 0 entities
        When we try to delete an entity from graph
        Then an exception occured

    Scenario Outline: Deleting link from graph
        Given a graph named "test"
        And the graph has <ne> entities
        And the graph has <ns> links
        When we delete a link from graph
        Then the graph has <nd> links

        Examples:
            |ne|ns|nd|
            |4 |1 |0 |
            |2 |3 |2 |
            |2 |1 |0 |
            |77|4 |3 |

    Scenario: Creating link on empty graph
        Given a graph named "test"
        And the graph has 0 entities
        And the graph has 0 links
        When we try to delete a link from graph
        Then an exception occured

    Scenario: Writing an empty graph
        Given a graph named "test"
        And the graph has 0 entities
        And the graph has 0 links
        When we dump the graph into a string
        Then the string is valid JSON
        And the "entities" field is an empty table
        And the "links" field is an empty table
        And the name of the graph is "test"
        And a graph can be parsed from the JSON

    Scenario Outline: Writing a filled graph
        Given a graph named "<ng>"
        And the graph has <nbe> entities
        And the graph has <nbl> links
        When we dump the graph into a string
        Then the string is valid JSON
        And a graph can be parsed from the JSON

        Examples:
            |ng  |nbe|nbl|
            |test|3  |4  |
            |mdot|12 |0  |
