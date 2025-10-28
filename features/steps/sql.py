import os
from behave import *

from merise_dot.model.mcd import MCDLink
from merise_dot.dot.script import Script
from merise_dot.scripts import SQLConversionKernel
from merise_dot.scripts.mysql import MySQLCore

# TODO define a conversion core map
_CONVERSION_CORE_TABLE: dict[str | SQLConversionKernel] = {
    "MySQL": MySQLCore()
}


@given("{a:d} is linked to {b:d} by the cardinality ({cn:d},{cm})")
def establish_lk(context, a: int, b: int, cn: int, cm: str) -> None:
    lk: MCDLink = context.graph.get_link(f"l_{min(a, b) - 1}_{max(a, b) - 1}")
    m_card: int = -1 if cm == "n" else int(cm)
    lk.edit_card(context.graph.get_ent(f"e_{a}"), cn, m_card)


@given(
    "the link between {a:d} and {b:d} also links {c:d} by cardinality ({cn:d},{cm})"
)
def ternary(context, a: int, b: int, c: int, cn: int, cm: str) -> None:
    lk: MCDLink = context.graph.get_link(f"l_{min(a, b) - 1}_{max(a, b) - 1}")
    m_card: int = -1 if cm == "n" else int(cm)
    lk.add_card_str(f"e_{c - 1}", cn, m_card)


@when("we select {name} as a conversion kernel")
def core_selection(context, name: str) -> None:
    context.core = _CONVERSION_CORE_TABLE[name]


@when("we turn the MLD into an SQL script")
def convert_sql(context) -> None:
    context.script = Script(context.core)
    context.script.mk_sql(context.mld)


@then("the script is the same as \"{f_name}.sql\"")
def check_script(context, f_name: str) -> None:
    contents: str = ""
    with open(f"{os.getcwd()}/features/assets/{f_name}.sql", 'r') as file:
        contents = file.read()
    # TODO fetch output script for check
    output: str = str(context.script)
    assert output == contents
