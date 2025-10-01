import pzp

from merise_dot.model import Graph, EntityNotFoundException
from merise_dot.model.mcd import Entity
from .fields import *
from .scheme import *


class EntityEditOp(OpsScheme):

    def __init__(self) -> None:
        self._field_ops: dict[str | OpsScheme] = {
            "Adding a field": FieldAddOp()
        }

    def handle(self, graph: Graph, **kwargs) -> None:
        print("Select which entity to edit ;")
        name: str = pzp.pzp(
            graph._entities.keys,
            fullscreen=False,
            height=len(graph._entities) + 2)
        try:
            ent: Entity = graph.get_entity(name)
            print(f"Editing entity {name}")
            choice: str = pzp.pzp(
                self._field_ops.keys(),
                fullscreen=False,
                height=len(self._field_ops) + 2)
            self._field_ops[choice].handle(graph, entity=entity)
        except EntityNotFoundException as e:
            print(f"Couldn't edit entity {name} : {e}")
