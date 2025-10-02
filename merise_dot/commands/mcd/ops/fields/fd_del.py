import pzp

from merise_dot.model import Graph
from merise_dot.model.mcd import Entity, FieldNotFoundException
from merise_dot.commands.mcd.ops.scheme import *


class FieldDelOp(OpsScheme):

    def __init__(self) -> None:
        super().__init__()

    def handle(self, graph: Graph, **kwargs) -> None:
        entity: Entity = kwargs['entity']
        # command main code
        print("Which field do you want to delete ?")
        name: str = pzp.pzp(
            entity._fields.keys(),
            fullscreen=False,
            height=len(entity._fields) + 2)
        try:
            entity.delete_field(name)
            print(f"removed field {name} from entity {entity._name}")
        except FieldNotFoundException as e:
            print(f"Couldn't remove field : {e}")
