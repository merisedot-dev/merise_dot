import tempfile
from behave import *

from merise_dot.model.mcd import MCDLink, Entity
from merise_dot.dot import MCDBuilder


@given("each entity has a primary key")
def ensure_pk(context) -> None:
    for n, ent in context.graph._entities.items():
        ent.add_field(f"pk_{n}", "int", True)


@given("the entities {a:d} and {b:d} are linked")
def ensure_link(context, a: int, b: int) -> None:
    context.graph.add_link(f"lk_e{a-1}_e{b-1}", f"e_{a-1}", f"e_{b-1}")


@given("entity {e:d} has another field named \"{name}\"")
def ensure_another_field(context, e: int, name: str) -> None:
    context.graph                               \
        .get_entity(f"e_{e-1}")                 \
        .add_field("f_test", "string", False)


@given("the link between {l1:d} and {l2:d} has {nb:d} fields")
def ensure_link_fields(context, l1: int, l2: int, nb: int) -> None:
    glk: MCDLink = context.graph.get_link(f"lk_e{l1-1}_e{l2-1}")
    for i in range(nb):
        glk.add_field(f"lkf_{i}", "bigint")


@given("the link between {l1:d} and {l2:d} is also linked to {l3:d}")
def ensure_ternary_link(context, l1: int, l2: int, l3: int) -> None:
    glk: MCDLink = context.graph.get_link(f"lk_e{l1-1}_e{l2-1}")
    ent: Entity = context.graph.get_entity(f"e_{l3-1}")
    glk.add_card(ent, 0, 1)


@when("we compile the graph as DOT")
def dot_compile(context) -> None:
    context.mcdb = MCDBuilder()
    context.mcdb.mk_graph(context.graph)


@then("the DOT structure can be turned into an image")
def check_img(context) -> None:
    context.mcdb.build(tempfile.mktemp(dir="./test_files/"))
