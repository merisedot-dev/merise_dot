Feature: Linking entities together.

    Scenario: Link creation
        Given a graph named "mdot"
        And an entity named "test" in graph
        And another entity named "kitty" in graph
        When we try to link "kitty" and "test"
        Then the graph has 1 link
        And the link has 2 cardinalities
        And one cardinality of the link points to "test"
        And one cardinality of the link points to "kitty"

    Scenario Outline: A link is empty at creation
        When we create a link named "mdot"
        Then the link has no cardinalities

        Examples:
            |nb|
            |0 |
            |1 |
            |2 |
            |12[

    Scenario Outline: Removing cardinalities from link
        Given a link named "mdot"
        And the link has <nb> cardinalities
        When we remove <nc> cardinalities from link
        Then the link has <nd> cardinalities

        Examples:
            |nb|nc|nd|
            |0 |0 |0 |
            |3 |2 |1 |
            |3 |3 |0 |

    Scenario Outline: Adding specific fields to link entity
        Given a link named "mdot"
        And the link has <nbc> cardinalities
        When we add a field named "<name>" with type <t> to the link
        Then the link has 1 field(s)
        And the link field is named "<name>"
        And the link field is of type <t>

        Examples:
            |nbc|name  |t          |
            |3  |miaouh|int        |
            |0  |test  |varchar(40)|
            |10 |merise|date       |
