from behave import *


@given("we're using the {sgbd} converter")
def choose_converter(context, sgbd: str) -> None:
    context.sgbd = sgbd


@given("a new {cstype} constraint named \"{name}\"")
def ensure_constraint(context, cstype: str, name: str) -> None:
    pass


@given("the constraint uses field \"{fname}\"")
def ensure_inner_field(context, fname: str) -> None:
    pass


@given("the foreign key references the table {t2} on field {f2}")
def ensure_fk_refs(context, t2: str, f2: str) -> None:
    pass


@given("the constraint is applied to the table \"{table}\"")
def ensure_table(context, table: str) -> None:
    pass


@when("we turn the constraint into a string")
def cstr_to_str(context) -> None:
    pass
