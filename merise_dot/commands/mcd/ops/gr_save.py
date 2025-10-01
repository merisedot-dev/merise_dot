from merise_dot.model import Graph
from .scheme import *


class GraphSaveOp(OpsScheme):

    def __init__(self) -> None:
        super().__init__()

    def handle(self, graph: Graph, **kwargs) -> None:
        path: str = kwargs['path']
        # quick memory dump
        with open(path, 'w') as file:
            print("Saving MCD graph...")
            file.write(str(graph))
        print("Saved MCD graph")
