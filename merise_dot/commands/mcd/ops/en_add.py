import pzp

from merise_dot.model import Graph
from .scheme import *


class EntityAddOp(OpsScheme):

    def __init__(self) -> None:
        super().__init__()

    def handle(self, graph: Graph, **kwargs) -> None:
        name: str = pzp.prompt("Name of the entity to add")
        if not name:
            return # why, just, why ?
        try:
            graph.add_entity(name)
            print(f"Added entity {name}")
        except Exception as e:
            print(f"Couldn't add entity : {e}")
