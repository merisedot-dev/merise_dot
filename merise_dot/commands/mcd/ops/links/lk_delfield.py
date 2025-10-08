import pzp

from merise_dot.model import Graph
from merise_dot.model.mcd import MCDLink
from merise_dot.commands.mcd.ops.scheme import OpsScheme


class LinkFieldDeleteOp(OpsScheme):

    def __init__(self) -> None:
        super().__init__()

    def handle(self, graph: Graph, **kwargs) -> None:
        link: MCDLink = kwargs['link']
        # main command code
        print("Select field to remove :")
        f_name: str = pzp.pzp(link._fields.keys())
        try:
            link.del_field(f_name)
            print(f"Deleted field {f_name} from link {link._name}")
        except Exception as e:
            print(f"Couldn't delete field {f_name}: {e}")
