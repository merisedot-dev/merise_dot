from behave import *
from features.steps.aux import *

from merise_dot.scripts.cstr import *
from merise_dot.scripts.table import SQLTable, TableField, TableFieldType


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


@given("a new SQL table named \"{table}\"")
def adding_table(context, table: str) -> None:
    context.sql_table: SQLTable = SQLTable(table)


@given("the table has a primary key")
def table_mkpk(context) -> None:
    field = TableField(f"pk_{context.sql_table._name}", TableFieldType.INTEGER)
    field.pk() # it's not a PK otherwise
    context.sql_table.add_field(field)


@given("the table has {n:d} fields")
def table_nbfields(context, n: int) -> None:
    for i in range(n):
        context.sql_table.add_field(
            TableField(f"e_{i}", TableFieldType.INTEGER))


@given("a new unique constraint named \"{name}\"")
def mk_unq(context, name: str) -> None:
    context.constraint = UniqueConstraint(name)


@given("{nu:d} fields from the table are unique")
def unq_fields(context, nu: int) -> None:
    for i in range(nu):
        context.constraint.add_field(context.sql_table._fields[f"e_{i}"])


@when("we turn the constraint into a string")
def cstr_to_str(context) -> None:
    context.script = str(context.constraint)


@then("the constraint script looks like \"{path}.sql\"")
def check_cstr_script(context, path: str) -> None:
    check_script(context, f"constraints/{path}")
