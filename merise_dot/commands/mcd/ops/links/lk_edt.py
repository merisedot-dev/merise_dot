import questionary
from rich import print as rprint
from merise_dot.dot import mk_link_richtable
from merise_dot.model import Graph
from merise_dot.model.mcd import MCDLink


def link_edit_card(graph: Graph, link: MCDLink) -> None:
    rprint(mk_link_richtable(link))
    card_name: str = questionary.select(
        "Which cardinality do you want to edit ?",
        choices=link._entities.keys()).ask()
    c_min, c_max = link.get_card(card_name)
    # define minimum cardinality
    card_min: int = questionary.text(
        "Minimum cardinality (-1 is n)", default=0).ask()
    # define maximum cardinality
    card_max: int = questionary.text(
        "Maximum cardinality (-1 is n)", default=0).ask()
    # changing cardinality
    link.del_card_str(card_name)
    link.add_card_str(card_name, card_min, card_max)
    # acknowledging
    rprint(f"Cardinality {card_name} set to ({card_min},{card_max})")
