Feature: SQL conversion of a graph

    Scenario Outline: Empty graph
        Given a graph named "<name>"
        And the graph has 0 entities
        And the graph has 0 links
        And the graph is turned into an MLD
        When we select <core> as a conversion kernel
        And we turn the MLD into an SQL script
        Then the script is the same as "<name>.sql"

        Examples:
            |name|core |
            |mdot|MySQL|

    Scenario Outline: Only entities
        Given a graph named "<name>"
        And the graph has <ne> entities
        And each entity has a primary key
        And the graph has 0 links
        And the graph is turned into an MLD
        When we select <core> as a conversion kernel
        And we turn the MLD into an SQL script
        Then the script is the same as "<name>.sql"

        Examples:
            |name|ne|core |
            |test|5 |MySQL|
            |t2  |10|MySQL|
            |t3  |1 |MySQL|

    Scenario Outline: Full on database
        Given a graph named "<name>"
        And the graph has 5 entities
        And each entity has a primary key
        And the graph is turned into an MLD
        When we select <core> as a conversion kernel
        And we turn the MLD into an SQL script
        Then the script is the same as "<name>.sql"

        Examples:
            |name  |core |
            |mgraph|MySQL|
