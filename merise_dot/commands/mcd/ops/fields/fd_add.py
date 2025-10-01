import pzp

from merise_dot.model import Graph
from merise_dot.model.mcd import Entity
from merise_dot.commands.mcd.ops.scheme import *


class FieldAddOp(OpsScheme):

    def __init__(self) -> None:
        super().__init__()

    def handle(self, graph: Graph, **kwargs) -> None:
        entity: Entity = kwargs['entity']
        # checking name
        name: str = pzp.prompt("Name of the field to add")
        if not name:
            return
        # checking type (no spellcheck yet)
        f_type: str = pzp.prompt("Type of the field")
        if not f_type:
            return
        # checking is field should be primary
        try:
            pass
        except:
            pass
