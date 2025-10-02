import pzp

from merise_dot.model import Graph
from merise_dot.model.mcd import MCDLink
from merise_dot.commands.mcd.ops.scheme import OpsScheme


class LinkEditCardOp(OpsScheme):

    def __init__(self) -> None:
        super().__init__()

    def handle(self, graph: Graph, **kwargs) -> None:
        link: MCDLink = kwargs['link']
        # main command code
        print("Choose which cardinality to edit")
        name: str = pzp.pzp(
            link._entities.keys(),
            fullscreen=False,
            height=len(link._entities) + 2)
        c_min, c_max = link.get_card(name)
        # eiditing values on the cardinality
        ca_min: int = pzp.prompt(
            f"Minimum cardinality (default {c_min})", default=c_min)
        ca_max: int = pzp.prompt(
            f"Maximum cardinality (default n)", default=-1)
        # actual edition
        try:
            link.del_card_str(name)
            link.add_card_str(name, ca_min, ca_max)
            print(f"Edited cardinality {name}")
        except:
            print(f"Couldn't edit cardinality : {e}")
