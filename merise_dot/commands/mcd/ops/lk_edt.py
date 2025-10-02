import pzp

from merise_dot.model import Graph
from merise_dot.model.mcd import MCDLink
from .links import *
from .scheme import *


class LinkEditOp(OpsScheme):

    def __init__(self) -> None:
        super().__init__()
        self._edit_op: dict[str | OpsScheme] = {
            "Add cardinality": LinkAddCardOp(),
            "Edit cardinality": LinkEditCardOp(),
            "Delete cardinality": LinkDelCardOp()
        }

    def handle(self, graph: Graph, **kwargs) -> None:
        print("Choose which link to edit")
        name: str = pzp.pzp(
            graph._links.keys(),
            fullscreen=False,
            height=len(graph._links) + 2)
        link: MCDLink = graph.get_link(name)
        # TODO select edit op
        choice: str = pzp.pzp(
            self._edit_op.keys(),
            fullscreen=False,
            height=len(self._edit_op.keys()) + 2)
        self._edit_op[choice].handle(graph, link=link)
