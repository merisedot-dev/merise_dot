import questionary
from merise_dot.model import Graph


def del_entity_op(graph: Graph) -> None:
    name: str = questionary.text(
        "Choose the entity to delete from MCD :",
        choices=graph._entities.keys()).ask()
    # small guard clause
    if not graph.get_entity(name):
        rprint(f"Entity {name} isn't in MCD")
        return
    # actual deletion
    check: bool = questionary.confirm(
        f"Deleting {name} may cause cascading deletions. Continue ? [y/n]"
    ).ask()
    if check: # cascade deletion was confirmed
        graph.del_entity(name)
        rprint(f"Entity {name} has been deleted")
