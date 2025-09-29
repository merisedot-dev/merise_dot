import questionary
from rich import print as rprint
from merise_dot.model import Graph


def add_entity_op(graph: Graph) -> None:
    try:
        ent = graph.add_entity(
            questionary.question("Enter new Entity name :").ask())
        rprint(f"Entity {ent._name} has been added to MCD")
    except:
        rprint("Couldn't add entity. The name was taken")
