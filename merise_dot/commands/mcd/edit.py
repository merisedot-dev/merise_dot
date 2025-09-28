import questionary
from rich import print as rprint

# inner imports
from merise_dot.model import Graph
from .ops import *

# constants, please do not touch
_OPS_CHOICES = {
    "add an entity": add_entity_ops,
    "edit an entity": edit_entity_op,
    "delete an entity": del_entity_op,
    "link two entities": link_entity_op
}


def edit_graph(graph: Graph) -> None:
    while True: # it's a mainloop
        qst: str = questionary.select(
            "Choose an operation to perform",
            choices=_OPS_CHOICES.keys()).ask()
        _OPS_CHOICES[qst](graph)
        # TODO save graph to file before losing it
