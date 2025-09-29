import questionary
from merise_dot.model import Graph
from .fields import *

# functer trick
_FIELD_OPS_CHOICES = {
    "add a field": add_field_op,
    "edit a field": edit_field_op
}


def edit_entity_op(graph: Graph) -> None:
    en_name: str = questionary.select(
        "Choose the entity to edit", choices=graph._entities.keys()).ask()
    op: str = questionary.select(
        "What do you want to do with the entity ?",
        choices=_FIELD_OPS_CHOICES.keys()).ask()
    _FIELD_OPS_CHOICES[op](graph.get_entity(en_name))
