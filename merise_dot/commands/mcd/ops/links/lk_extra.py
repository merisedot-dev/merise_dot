import questionary
from rich import print as rprint
from merise_dot.model import Graph
from merise_dot.model.mcd import Entity, MCDLink


def link_extra_op(graph: Graph, lk: MCDLink) -> None:
    try:
        lk.add_card(
            graph.get_entity(
                str(
                    questionary.select(
                        "Which extra entity to link",
                        choices=graph._entities.keys()).ask())),
            int(questionary.question("Minimum cardinality :").ask()),
            int(
                questionary.question(
                    "Maximum cardinality (-1 is 'n') :").ask()))
    except Exception as e:
        rprint(f"A problem occured during linking : {e}")
