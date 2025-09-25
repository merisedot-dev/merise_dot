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
