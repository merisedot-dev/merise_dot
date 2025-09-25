import tempfile
from behave import *
from merise_dot.dot import MCDBuilder


@when("we compile the graph as DOT")
def dot_compile(context) -> None:
    context.mcdb = MCDBuilder()
    context.mcdb.mk_graph(context.graph)


@then("the DOT structure can be turned into an image")
def check_img(context) -> None:
    context.mcdb.build(tempfile.mktemp())
