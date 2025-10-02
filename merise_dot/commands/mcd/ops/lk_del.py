import pzp

from merise_dot.model import Graph
from .scheme import *


class LinkDeleteOp(OpsScheme):

    def __init__(self) -> None:
        super().__init__()

    def handle(self, graph: Graph, **kwargs) -> None:
        print("Choose which link to delete")
        name: str = pzp.pzp(
            graph._links.keys(),
            fullscreen=False,
            height=len(graph._links) + 2)
        if not pzp.confirm(f"Are you sure you want to delete {name} ?"):
            return
        graph._links.pop(name)
        print(f"Deleted link {name} from graph")
