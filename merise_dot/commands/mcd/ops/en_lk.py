import pzp, questionary
from rich import print as rprint
from merise_dot.model import Graph
from merise_dot.model.mcd import MCDLink
from .links import *

# extra constants
_LK_OPS = {
    "link an extra entity": lk_extra,
    "remove cardinalities from link": link_remove_op,
    "edit a link's cardinality": link_edit_card
}


def link_entity_op(graph: Graph) -> None:
    # choice setup
    en_choices: list[str] = []
    for _, mcd_link in graph._links.items():
        # this may tank complexity, but it's a CLI, users are more patient
        for e_name in mcd_link._entities.keys():
            if not (e_name in en_choices):
                en_choices.append(e_name)
    # entity selection
    chs: list[str] = questionary.checkbox(
        "Select one or two linked entities :", choices=en_choices).ask()
    if len(chs) == 0:
        return # just... WHY ?
    en_0, en1 = chs[0], chs[0] if len(chs) == 1 else chs[1]
    # make a second choice salvo to select our link
    lk_choices: dict[str | MCDLink] = {}
    for _, mcd_link in graph._links.items():
        if en_0 in mcd_link._entities.keys(
        ) and en1 in mcd_link._entities.keys():
            lk_choices[mcd_link._name] = mcd_link
    # link selection
    mcd_link: MCDLink = lk_choices[questionary.select(
        "Choose a link for your entities :", choices=lk_choices).ask()]
    # select operation
    _LK_OPS[questionary.select(
        "Choose what do with the link :",
        choices=_LK_OPS).ask()](graph, mcd_link)
