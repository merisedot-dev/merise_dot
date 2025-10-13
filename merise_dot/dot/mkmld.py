from merise_dot.model.mcd import Graph
from merise_dot.model.mld import MLDGraph


class MLDBuilder:

    def __init__(self) -> None:
        self._name: str = ""
        self._graph: MLDGraph = None

    def mk_graph(self, graph: Graph) -> None:
        """Turn an MCD graph into an MLD one.
        We're not checking if the graph is well formed, as inner methods from the
        MCD graph should already have kicked in and crashed out.

        :param graph: the graph to convert.
        """
        self._name = graph._name

    def get(self) -> MLDGraph:
        """Fetched the transformed graph.

        :returns: The processed MLD graph. None if no processing occured.
        """
        return self._graph
