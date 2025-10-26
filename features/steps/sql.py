from behave import *

from merise_dot.dot.script import Script
from merise_dot.scripts import SQLConversionKernel
from merise_dot.scripts.mysql import MySQLCore

# TODO define a conversion core map
_CONVERSION_CORE_TABLE: dict[str | SQLConversionKernel] = {
    "MySQL": MySQLCore()
}


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
    with open(f"assets/{f_name}.sql", 'r') as file: # FIXME
        contents = file.read()
    # TODO fetch output script for check
    output: str = str(context.script)
    assert output == contents
