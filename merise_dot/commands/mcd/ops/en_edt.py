import questionary
from merise_dot.model import Graph


def edit_entity_op(graph: Graph) -> None:
    en_name: str = questionary.select(
        "Choose the entity to edit", choices=graph._entities.keys()).ask()
    # TODO define ops for entity edition
    # TODO call the damn things
