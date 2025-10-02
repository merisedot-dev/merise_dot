import pzp

from merise_dot.model import Graph
from merise_dot.model.mcd import Entity, FieldNotFoundException
from merise_dot.commands.mcd.ops.scheme import *


class FieldEditOp(OpsScheme):

    def __init__(self) -> None:
        super().__init__()

    def handle(self, graph: Graph, **kwargs) -> None:
        entity: Entity = kwargs['entity']
        # main command code
        print("Which field do you want to edit ?")
        name: str = pzp.pzp(
            entity._fields.keys(),
            fullscreen=False,
            height=len(entity._fields) + 2)
        f_type, prim = entity.get_field(name)
        # field values edition section
        f_type = pzp.prompt(
            f"New type for the field (default {f_type})", default=f_type)
        prim = pzp.confirm("Make field primary ?")
        try:
            entity.edit_field(name, f_type, prim)
            print(f"Edited field {name} with values : ({f_type},{prim})")
        except FieldNotFoundException as e:
            print(f"Couldn't edit field : {e}")
