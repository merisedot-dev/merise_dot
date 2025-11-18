import os
from behave import *

from merise_dot.model.mcd import MCDLink
from merise_dot.dot.script import Script
from merise_dot.scripts import SQLConversionKernel, SQLTable, TableField, TableFieldType
from merise_dot.scripts.mysql import MySQLCore

# TODO define a conversion core map
_CONVERSION_CORE_TABLE: dict[str | SQLConversionKernel] = {
    "MySQL": MySQLCore()
}


@given("{a:d} is linked to {b:d} by the cardinality ({cn:d},{cm})")
def establish_lk(context, a: int, b: int, cn: int, cm: str) -> None:
    lk: MCDLink = context.graph.get_link(f"l_{min(a, b) - 1}_{max(a, b) - 1}")
    m_card: int = -1 if cm == "n" else int(cm)
    lk.edit_card(context.graph.get_entity(f"e_{a - 1}"), cn, m_card)


@given(
    "the link between {a:d} and {b:d} also links {c:d} by cardinality ({cn:d},{cm})"
)
def ternary(context, a: int, b: int, c: int, cn: int, cm: str) -> None:
    lk: MCDLink = context.graph.get_link(f"l_{min(a, b) - 1}_{max(a, b) - 1}")
    m_card: int = -1 if cm == "n" else int(cm)
    lk.add_card_str(f"e_{c - 1}", cn, m_card)


@given("a SQL table named \"{name}\"")
def mk_table(context, name: str) -> None:
    context.sql_table = SQLTable(name)


def insert_fields(context, nb: int, f_type: TableFieldType) -> None:
    for i in range(nb):
        context.sql_table.add_field(TableField(f"f_{f_type}_{i}", f_type))


@given("the table has {nb:d} integer fields")
def insert_int_fields(context, nb: int) -> None:
    insert_fields(context, nb, TableFieldType.INTEGER)


@given("the table has {nb:d} bigint fields")
def insert_bigint_fields(context, nb: int) -> None:
    insert_fields(context, nb, TableFieldType.BIGINT)


@given("the table has {nb:d} boolean fields")
def insert_bool_fields(context, nb: int) -> None:
    insert_fields(context, nb, TableFieldType.BOOLEAN)


@given("the table has {nb:d} uuid fields")
def insert_uid_fields(context, nb: int) -> None:
    insert_fields(context, nb, TableFieldType.UUID)


@when("we select {name} as a conversion kernel")
def core_selection(context, name: str) -> None:
    context.core = _CONVERSION_CORE_TABLE[name]


@when("we turn the MLD into an SQL script")
def convert_sql(context) -> None:
    context.script = Script(context.core)
    context.script.mk_sql(context.mld)


@when("we turn the table into script")
def convert_table(context) -> None:
    context.script = str(context.sql_table)


@then("the script piece looks like the script in \"{f_name}.sql\"")
@then("the script is the same as \"{f_name}.sql\"")
def check_script(context, f_name: str) -> None:
    contents: str = ""
    with open(f"{os.getcwd()}/features/assets/{f_name}.sql", 'r') as file:
        contents = file.read().strip().replace('    ', '\t') # space constraint
    output: str = str(context.script)
    print(str(contents))
    assert output == contents


@then("the table script is the same as \"{f_name}.sql\"")
def check_table_script(context, f_name: str) -> None:
    check_script(context, f"tables/{f_name}")
