import pzp

from merise_dot.model import Graph
from .ops import *


class MCDEditCmd:

    def __init__(self) -> None:
        self._edit_ops: dict[str | OpsScheme] = {
            "Add an entity": EntityAddOp(),
            "Edit an entity": EntityEditOp(),
            "Delete an entity": EntityDelOp(),
            "Link two entities": LinkAddOp(),
            "Save graph": GraphSaveOp(),
            "Exit": ExitOp()
        }

    def edit(self, graph: Graph, path: str) -> None:
        while True:
            print("Select what to do with the graph :")
            choice: str = pzp.pzp(
                self._edit_ops.keys(),
                fullscreen=False,
                height=len(self._edit_ops) + 2)
            self._edit_ops[choice].handle(graph, path=path)
