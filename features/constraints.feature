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
