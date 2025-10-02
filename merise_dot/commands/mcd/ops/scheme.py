from merise_dot.model import Graph


class OpsScheme:

    def __init__(self) -> None:
        if type(self) == "OpsScheme":
            raise Exception("this is abstract")

    def handle(self, graph: Graph, **kwargs) -> None:
        if type(self) != "OpsScheme":
            raise Exception("this is abstract")
