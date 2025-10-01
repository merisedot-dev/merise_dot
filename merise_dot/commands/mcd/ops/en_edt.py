from merise_dot.model import Graph
from .scheme import *


class EntityEditOp(OpsScheme):

    def __init__(self) -> None:
        super().__init__()

    def handle(self, graph: Graph, **kwargs) -> None:
        pass
