import pzp

from merise_dot.model import Graph
from merise_dot.model.mcd import MCDLink
from merise_dot.commands.mcd.ops.scheme import OpsScheme


class LinkFieldEdtOp(OpsScheme):

    def __init__(self) -> None:
        super().__init__()

    def handle(self, graph: Graph, **kwargs) -> None:
        link: MCDLink = kwargs['link']
        # main command code
        print("Select the field to edit :")
        f_name: str = pzp.pzp(link._fields.keys())
        f_type: str = pzp.prompt(
            f"Enter new field type (default {link.get_field(f_name)})",
            default=link.get_field(f_name))
        try:
            link.del_field(f_name)
            link.add_field(f_name, f_type)
            print(f"Set field {f_name} to {f_type}")
        except Exception as e:
            print(f"Couldn't edit field {f_name}: {e}")
