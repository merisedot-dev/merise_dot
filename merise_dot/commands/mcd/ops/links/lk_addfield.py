import pzp

from merise_dot.model import Graph
from merise_dot.model.mcd import MCDLink
from merise_dot.commands.mcd.ops.scheme import OpsScheme


class LinkAddFieldOp(OpsScheme):

    def __init__(self) -> None:
        super().__init__()

    def handle(self, graph: Graph, **kwargs) -> None:
        link: MCDLink = kwargs['link']
        # main ops code
        print(f"Current fields :\n{"\n".join(
            f"\t{name}" for name in link._fields.keys())}")
        # questions
        name: str = pzp.prompt("Enter name of the field to add")
        f_type: str = pzp.prompt(f"Enter type of field {name}")
        try:
            link.add_field(name, f_type)
        except Exception as e:
            print(f"Couldn't insert field {name} : {e}")
