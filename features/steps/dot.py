import tempfile
from behave import *
from merise_dot.dot import MCDBuilder


@given("each entity has a primary key")
def ensure_pk(context) -> None:
    for n, ent in context.graph._entities.items():
        ent.add_field(f"pk_{n}", "string", True)


@given("the entities {a:d} and {b:d} are linked")
def ensure_link(context, a, b) -> None:
    context.graph.add_link(f"l_{a-1}.{b-1}", f"e_{a-1}", f"e_{b-1}")


@when("we compile the graph as DOT")
def dot_compile(context) -> None:
    context.mcdb = MCDBuilder()
    context.mcdb.mk_graph(context.graph)


@then("the DOT structure can be turned into an image")
def check_img(context) -> None:
    context.mcdb.build(tempfile.mktemp(dir="./test_files/"))
