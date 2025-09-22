from behave import given
from merisedot.model import Graph


@given("the graph currently does not exist")
def no_graph(context) -> None:
    context.graph = None


@given("a graph named \"{name:s}\"")
def init_graph(context, name: str) -> None:
    context.graph = Graph(name)


@given("the graph has {n:d} entities")
def init_entities(context, n: int) -> None:
    context.graph._entities = {}
    for i in range(n):
        context.graph.add_entity(f"e_{i}")
