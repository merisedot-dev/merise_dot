from behave import *
from merise_dot.dot import MCDBuilder


@when("we compile the graph as DOT")
def dot_compile(context) -> None:
    mcdb = MCDBuilder()
    mcdb.mk_graph(context.graph)


@then("a DOT structure is returned")
def check_dot(context) -> None:
    assert False


@then("the DOT structure can be turned into an image")
def check_img(context) -> None:
    assert False
