import pzp

from merise_dot.model import Graph
from merise_dot.model.mcd import MCDLink
from merise_dot.commands.mcd.ops.scheme import OpsScheme


class LinkDelCardOp(OpsScheme):

    def __init__(self) -> None:
        super().__init__()

    def handle(self, graph: Graph, **kwargs) -> None:
        link: MCDLink = kwargs['link']
        # main command code
        print("Select cardinality to delete")
        name: str = pzp.pzp(
            link._entities.keys(),
            fullscreen=False,
            height=len(link._entities) + 2)
        if not pzp.confirm(
                f"Are you sure you want to delete cardinality {name} ?"):
            return
        try:
            link.del_card_str(name)
            print(f"Deleted cardinality on {name}")
        except Exception as e:
            print(f"Couldn't delete cardinality : {e}")
