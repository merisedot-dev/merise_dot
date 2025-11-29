Feature: MLD conversion from MCD graph.

    Scenario Outline: No linked entities in graph
        Given a graph named "mdot"
        And the graph has <nb> entities
        And the graph has 0 links
        When we turn the graph into an MLD
        Then the MLD has <nb> entities
        And the MLD has 0 links

        Examples:
            |nb    |
            |0     |
            |87    |
            |161501|
            |159700|
            |2     |

    Scenario Outline: 1,n associations
        Given a graph named "mdot"
        And the graph has an entity named "test1"
        And the graph has an entity named "test2"
        And the entity "test1" has a primary key
        And the entity "test2" has a primary key
        And the entities "test1" and "test2" are linked
        And the cardinality on "test1" is (<min11>,<min21>)
        And the cardinality on "test2" is (<min12>,<min22>)
        When we turn the graph into an MLD
        Then the MLD has an entity named "test1"
        And the MLD has an entity named "test2"
        And the entity "<point1>" has a foreign key to "<point2>"

        Examples:
            |min11|min21|min12|min22|point1|point2|
            |0    |1    |0    |n    |test1 |test2 |
            |0    |n    |0    |1    |test2 |test1 |

    Scenario: n,n association
        Given a graph named "mdot"
        And the graph has an entity named "test1"
        And the graph has an entity named "test2"
        And the entity "test1" has a primary key
        And the entity "test2" has a primary key
        And the entities "test1" and "test2" are linked
        And the cardinality on "test1" is (0,n)
        And the cardinality on "test2" is (0,n)
        When we turn the graph into an MLD
        Then the MLD has an entity named "test1"
        And the MLD has an entity named "test2"
        And the MLD has an entity named "lk_test1_test2"
        And the entity "lk_test1_test2" has a foreign key to "test1"
        And the entity "lk_test1_test2" has a foreign key to "test2"


    Scenario Outline: 0,1 associations
        Given a graph named "mdot"
        And the graph has an entity named "test1"
        And the graph has an entity named "test2"
        And the entity "test1" has a primary key
        And the entity "test2" has a primary key
        And the entities "test1" and "test2" are linked
        And the cardinality on "test1" is (<c1>,1)
        And the cardinality on "test2" is (<c2>,1)
        When we turn the graph into an MLD
        Then the MLD has an entity named "test1"
        And the MLD has an entity named "test2"
        And the entity "test1" has a foreign key to "test2"
        And the entity "test2" has a foreign key to "test1"

        Examples:
            |c1|c2|
            |1 |0 |
            |0 |1 |


    Scenario Outline: Field preservation
        Given a graph named "mdot"
        And the graph has an entity named "test"
        And the entity "test" has <nbf> fields
        And the entity "test" <status> a primary key
        When we turn the graph into an MLD
        Then the MLD has an entity named "test"
        And the MLD entity "test" has <nbfm> fields
        And the MLD entity "test" <status> a primary key

        Examples:
            |nbf|status|nbfm|
            |0  |hasn't|0   |
            |1  |has   |2   |
            |12 |has   |13  |
            |15 |hasn't|15  |

    Scenario Outline: Nullable links
        Given a graph named "mdot" 
        And the graph has an entity named "t1"
        And the graph has an entity named "t2"
        And each entity has a primary key
        And "t1" is linked to "t2" by the cardinality (<na>,<ma>)
        And "t2" is linked to "t1" by the cardinality (<nb>,<mb>)
        When we turn the graph into an MLD
        Then the MLD has 2 entities 
        And the entity "t1" has a foreign key to "t2" (<st1>)
        And this field is nullable (<nla>)
        And the entity "t2" has a foreign key to "t1" (<st2>)
        And this field is nullable (<nlb>)
  
        Examples:  
            |na|ma|nb|mb|st1|nla|st2|nlb|
            |0 |1 |0 |n |yes|yes|no |no |
            |0 |n |0 |1 |no |no |yes|yes|
            |1 |1 |0 |n |yes|no |no |no |
            |0 |n |1 |1 |no |no |yes|no |
  
    Scenario Outline: Extraneous link entities.
        Given a graph named "mdot"  
        And the graph has an entity named "t1"
        And the graph has an entity named "t2"
        And each entity has a primary key
        And "t1" is linked to "t2" by the cardinality (<na>,<ma>)
        And "t2" is linked to "t1" by the cardinality (<nb>,<mb>)
        When we turn the graph into an MLD
        Then the MLD has 3 entities
        And the entity "t1" has a foreign key to "t2" (no)
        And the entity "t2" has a foreign key to "t1" (no)
        And the entity "lk_t1_t2" has a foreign key to "t1" (yes)
        And this field is nullable (no)
        And the entity "lk_t1_t2" has a foreign key to "t2" (yes)
        And this field is nullable (no)

        Examples:
            |na|ma|nb|mb|
            |0 |n |0 |n |
