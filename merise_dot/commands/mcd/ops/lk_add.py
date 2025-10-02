import pzp

from merise_dot.model import Graph, LinkDuplicataException
from merise_dot.model.mcd import Entity
from .scheme import *


class LinkAddOp(OpsScheme):

    def __init__(self) -> None:
        super().__init__()

    def pick_ent(self, graph: Graph, msg: str) -> Entity:
        print(msg)
        name: str = pzp.pzp(
            graph._entities.keys(),
            fullscreen=False,
            height=len(graph._entities) + 2)
        return graph.get_entity(name)

    def handle(self, graph: Graph, **kwargs) -> None:
        name: str = pzp.prompt("Name of the link to add")
        if not name:
            return
        # choosing entities to link
        en1: Entity = self.pick_ent(graph, "Choose first entity to link")
        en2: Entity = self.pick_ent(
            graph, "Choose the other entity on the link")
        try:
            graph.add_link(name, en1, en2)
            print(f"Added link {name} for {en1._name} and {en2._name}")
        except LinkDuplicataException as lke:
            print(f"Couldn't add link {name} : {lke}")
