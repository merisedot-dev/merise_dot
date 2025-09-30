import questionary
from rich import print as rprint
from merise_dot.dot import mk_link_richtable
from merise_dot.model import Graph
from merise_dot.model.mcd import MCDLink


def link_remove_op(graph: Graph, link: MCDLink) -> None:
    rprint(mk_link_richtable(link))
    card_name: str = questionary.select(
        "Which cardinality do you want to remove ?",
        choices=link._entitites.keys()).ask()
    link.del_card_str(card_name)
    rprint(f"Cardinality on {card_name} removed")
