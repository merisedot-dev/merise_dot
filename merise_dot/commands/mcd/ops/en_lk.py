import questionary
from rich import print as rprint
from merise_dot.model import Graph


def link_entity_op(graph: Graph) -> None:
    en_choices: list[str] = graph._entities.keys()
    try:
        graph.add_link(
            questionary.question("Link name :").ask(),
            questionary.select("Choose the first entity",
                               choices=en_choices).ask(),
            questionary.select("Choose the second entity",
                               choices=en_choices).ask())
        # TODO upgrade to set your own cardinalities
    except:
        rprint("Link couldn't be created")
