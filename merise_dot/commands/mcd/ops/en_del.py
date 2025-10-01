import pzp

from merise_dot.model import Graph, EntityNotFoundException
from .scheme import *


class EntityDelOp(OpsScheme):

    def __init__(self) -> None:
        super().__init__()

    def handle(self, graph: Graph, **kwargs) -> None:
        if len(graph._entities) == 0:
            return
        name: str = pzp.pzp(
            graph._entities.keys(),
            fullscreen=False,
            height=len(graph._entities) + 2)
        try:
            graph.del_entity(name)
            print(f"Deleted entity {name}")
        except EntityNotFoundException as e:
            print(f"Couldn't delete entity : {e}")
