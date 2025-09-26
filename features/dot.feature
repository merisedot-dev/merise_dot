Feature: DOT graph compilation

    Scenario: Compiling empty graph
        Given a graph named "mdot"
        And the graph has 0 entities
        And the graph has 0 links
        When we compile the graph as DOT
        Then the DOT structure can be turned into an image

    Scenario Outline: Compiling a graph with something in it
        Given a graph named "mdot"
        And the graph has <ne> entities
        And the graph has <nl> links
        When we compile the graph as DOT
        Then the DOT structure can be turned into an image

        Examples:
            |ne|nl|
            |1 |1 |
            |1 |0 |
            |45|0 |
            |45|12|

    Scenario: Full-on graph compilation
        Given a graph named "mdot"
        And the graph has 5 entities
        And each entity has a primary key
        And the entities 1 and 5 are linked
        And the entities 2 and 3 are linked
        And the entities 3 and 3 are linked
        And the entities 3 and 5 are linked
        And entity 2 has another field named "test"
        When we compile the graph as DOT
        Then the DOT structure can be turned into an image
