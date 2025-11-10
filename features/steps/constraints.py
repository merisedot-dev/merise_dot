from behave import *

from merise_dot.scripts.cstr.fk import *
from merise_dot.scripts.table import TableField, TableFieldType


@given("we're using the {sgbd} converter")
def choose_converter(context, sgbd: str) -> None:
    context.sgbd = sgbd


@given("a new foreign key constraint named \"{name}\"")
def ensure_constraint(context, name: str) -> None:
    context.constraint = ForeignKeyConstraint(name)


@given("the constraint uses field \"{fname}\"")
def ensure_inner_field(context, fname: str) -> None:
    field = TableField(fname, TableFieldType.INTEGER) # type is arbitrary
    context.constraint.origin(field)


@given("the foreign key references the table {t2} on field {f2}")
def ensure_fk_refs(context, t2: str, f2: str) -> None:
    table = SQLTable(t2)
    table.add_field(TableField(f2, TableFieldType.INTEGER))
    # tweaking constraint
    context.constraint.points_to(table)
    context.constraint.on_field(f2)


@given("the constraint is applied to the table \"{table}\"")
def ensure_table(context, table: str) -> None:
    context.constraint.set_table(table)


@when("we turn the constraint into a string")
def cstr_to_str(context) -> None:
    context.script = str(context.constraint)
