import pzp

from merise_dot.model import Graph
from merise_dot.model.mcd import MCDLink, Entity
from merise_dot.commands.mcd.ops import OpsScheme


class LinkAddCardOp(OpsScheme):

    def __init__(self) -> None:
        super().__init__()

    def handle(self, graph: Graph, **kwargs) -> None:
        link: MCDLink = kwargs['link']
        # cardinality definition
        print(f"Choose which entity to link to {link._name}")
        ent: Entity = graph.get_entity(
            pzp.pzp(
                graph._entities.keys(),
                fullscreen=False,
                height=len(graph._entities) + 2))
        try:
            # cardinality choices
            card_min: int = int(
                pzp.prompt("Minimum cardinality (default 0)", default=0))
            card_max: int = int(
                pzp.prompt("Maximum cardinality (default n)", default=-1))
            # actual insertion
            link.add_card(ent, card_min, card_max)
            print(f"Added cardinality from {link._name} to {ent._name}")
        except Exception as e:
            print(f"Could't add cardinality : {e}")
