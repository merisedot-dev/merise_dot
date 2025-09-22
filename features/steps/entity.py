from behave import *
from merise_dot.model.mcd import Entity


@given("an entity named \"{name}\"")
@when("we create a new entity named \"{name}\"")
def make_entity(context, name: str) -> None:
    context.entity = Entity(name)


@given("a field named \"{fname}\"")
def set_field1(context, fname: str) -> None:
    context.e_field1_name = fname


@given("the field is of type {ftype}")
def set_field1_type(context, ftype: str) -> None:
    context.e_field1_type = ftype


@given("the field is primary ({primary})")
def set_field1_primary(context, primary: str) -> None:
    context.e_field1_primary = 1 if primary == "yes" else -1 if primary == "no" else 0


@when("the field is slotted into the entity")
def slot_field(context) -> None:
    context.entity.add_field(
        context.e_field1_name, context.e_field1_type, context.e_field1_primary)
