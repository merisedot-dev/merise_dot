Feature: Constraints management

    Scenario Outline: Foreign key
        Given we're using the <sgbd> converter
        And a new foreign key constraint named "<sgbd>_test_fk"
        And the constraint uses field "<fname>"
        And the foreign key references the table <t2> on field <f2>
        And the constraint is applied to the table "<table>"
        When we turn the constraint into a string
        Then the script piece looks like the script in "<sgbd>_fk_<table>.sql"

        Examples:
            |sgbd |table |fname|t2 |f2    |
            |MySQL|msql_t|truc |trg|pk_trg|

    Scenario Outline: Unique constraint
        Given we're using the <sgbd> converter
        And a new SQL table named "<table>"
        And the table has a primary key
        And the table has <n> fields
        And a new unique constraint named "<sgbd>_test_unq"
        And <nu> fields from the table are unique
        When we turn the constraint into a string
        Then the constraint script looks like "<sgbd>_unq_<table>.sql"

        Examples:
            |sgbd |table|n|nu|
            |MySQL|mdot |2|2 |
