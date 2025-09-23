Feature: MCD entity manipulation.

    Scenario: Creating a new Entity.
        When we create a new entity named "test"
        Then the entity's name is "test"
        And the entity has 0 fields

    Scenario Outline: Adding fields to an Entity.
        Given an entity named "<name>"
        And the entity has 0 fields
        And a field named "<fname>"
        And the field is of type <ftype>
        And the field is primary (<primary>)
        When the field is slotted into the entity
        Then the entity has a field named "<fname>"
        And the field is of type <ftype>
        And the field is primary(<primary>)

        Examples:
            |name |fname |ftype |primary|
            |test |ft    |bigint|no     |
            |kitty|nurgle|bool  |no     |
            |mdot |e3    |string|yes    |

    Scenario Outline: Adding multiple fields to an Entity.
        Given an entity named "<name>"
        And the entity has <nbi> fields
        When we add <nbm> more fields
        Then the entity has <nbf> fields

        Examples:
            |name|nbi|nbm|nbf|
            |test|3  |2  |5  |
            |mdot|77 |15 |92 |

    Scenario Outline: Deleting a specific field.
        Given an entity named "test"
        And a field with name "<fname>" in entity
        And a field with name "<fname2>" in entity
        When we delete the field "<fname>" from the entity
        Then the entity doesn't have a field named "<fname>"
        And the entity has a field named "<fname2>"

        Examples:
            |fname|fname2|
            |mdot |kitty |
            |chook|koohc |
