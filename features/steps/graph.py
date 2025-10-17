import json, random
from behave import *
from merise_dot.model import Graph, graph_parse
from merise_dot.model.mcd import Entity


@given("the graph currently does not exist")
def no_graph(context) -> None:
    context.graph = None


@given("a graph named \"{name}\"")
@when("we create a new graph named \"{name}\"")
def init_graph(context, name: str) -> None:
    context.graph = Graph(name)


@given("the graph has {n:d} entities")
def init_entities(context, n: int) -> None:
    for i in range(n):
        context.graph.add_entity(f"e_{i}")


@given("the graph has an entity named \"{name}\"")
@given("an entity named \"{name}\" in graph")
def g_init_spec_entity(context, name: str) -> None:
    context.graph.add_entity(name)


@given("the graph has {n:d} links")
def init_links(context, n: int) -> None:
    for i in range(n):
        a = random.randint(0, len(context.graph._entities) - 1)
        b = random.randint(0, len(context.graph._entities) - 1)
        context.graph.add_link(f"l_{i}", f"e_{a}", f"e_{b}")


@given("a link named \"{name}\" in graph")
def ensure_lk(context, name: str) -> None:
    for e_name in context.graph._entities.keys():
        context.graph.add_link(name, e_name, e_name)
        return # dirty hack


@given("the link points to \"{name}\"")
def ensure_lk_points(context, name: str) -> None:
    for _, lk in context.graph._links.items():
        lk.add_card_str(context.graph.get_entity(name), 0, -1)
        return # smol hack


@given("another entity named \"{name}\" in graph")
@when("we add an entity named \"{name}\"")
def add_one_entity(context, name: str) -> None:
    context.graph.add_entity(name)


@when("we delete an entity from graph")
def remove_one_entity(context) -> None:
    context.graph._entities.popitem()


@when("we delete a link from graph")
def remove_one_link(context) -> None:
    context.graph._links.popitem()


@when("we try to delete an entity from graph")
def attempt_remove_entity(context) -> None:
    try:
        context.graph._entities.popitem()
    except Exception:
        context.exception = Exception


@when("we try to delete a link from graph")
def attempt_remove_link(context) -> None:
    try:
        context.graph._links.popitem()
    except Exception:
        context.exception = Exception


@when("we fetch the \"{name}\" entity")
def g_get_entity(context, name: str) -> None:
    context.g_entity = context.graph.get_entity(name)


@when("we dump the graph into a string")
def dump_graph(context) -> None:
    context.g_dump = str(context.graph)


@when("we try to link \"{ea}\" and \"{eb}\"")
def lk_link(context, ea: str, eb: str) -> None:
    context.graph.add_link("lk_test", ea, eb)


@when("we remove the entity \"{name}\" from graph")
def rm_ent(context, name: str) -> None:
    context.graph.del_entity(name)


@then("the graph exists")
def check_graph(context) -> None:
    assert context.graph


@then("the graph name is \"{name}\"")
def check_graph_name(context, name: str) -> None:
    assert context.graph._name == name


@then("the graph has {n:d} entities")
@then("the graph has {n:d} entity")
def check_graph_entities(context, n: int) -> None:
    assert len(context.graph._entities) == n


@then("the graph has {n:d} link")
@then("the graph has {n:d} links")
def check_graph_links(context, n: int) -> None:
    assert len(context.graph._links) == n
    for l_name in context.graph._links.keys():
        context.lk = context.graph._links[l_name]
        return # another hack


@then("an exception occured")
def crash_happened(context) -> None:
    assert context.exception


@then("an entity is returned")
def g_got_entity(context) -> None:
    assert context.g_entity


@then("the name of the entity is \"{name}\"")
def g_entity_name(context, name: str) -> None:
    assert context.g_entity._name == name


@then("the string is valid JSON")
def is_json(context) -> None:
    context.json_g_dump = json.loads(context.g_dump)


@then("the \"{tname}\" field is an empty table")
def e_table_empty(context, tname: str) -> None:
    assert context.json_g_dump[tname] == []


@then("the name of the graph is \"{name}\"")
def check_dump_graph_name(context, name: str) -> None:
    assert context.json_g_dump["name"] == name


@then("a graph can be parsed from the JSON")
def check_valid_JSON(context) -> None:
    graph_parse(context.g_dump)


@then("the link \"{lk_name}\" is not pointing to \"{e_name}\"")
def check_lk_not_point(context, lk_name: str, e_name: str) -> None:
    assert not (context.graph.get_link(lk_name).get_card(e_name))
