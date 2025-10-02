from merise_dot.model import Graph
from .scheme import *


class ExitOp(OpsScheme):

    def __init__(self) -> None:
        super().__init__()

    def handle(self, graph: Graph, **kwargs) -> None:
        print("Closing program...")
        exit(0)
