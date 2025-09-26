from graphviz import Graph as GGraph
from merise_dot.model import Graph
from merise_dot.model.mcd import Entity, MCDLink

# Constants (please do not touch)
EDGE_SETTINGS: str = "edge [\nlen=2\nlabeldistance=2\n];"


class MCDBuilder:

    def __init__(self) -> None:
        self._name: str = ""
        self._info: GGraph = GGraph()

    def _mk_link(self, lk: MCDLink) -> None:
        self._info.node(lk._name, shape="Mrecord")
        for e_n, (min, max) in lk._entities.items():
            self._info.edge(
                lk._name, e_n, label=f"{min},{"n" if max==-1 else max}")

    def mk_graph(self, graph: Graph) -> None:

        def frm_ent(ent: Entity) -> str:
            return f"""{{
                \\N|{"\\l ".join(
                    f"{"PK " if f_p else "\t"}{f_n}: {f_t}"
                    for f_n,(f_t,f_p) in ent._fields.items())}\\l
                }}"""

        self._info = GGraph(graph._name)
        # entities
        for _, ent in graph._entities.items():
            self._info.node(ent._name, label=frm_ent(ent), shape="record")
        # links
        for _, lk in graph._links.items():
            self._mk_link(lk)

    def build(self, path: str) -> None:
        self._info.format = "png"
        self._info.render(path)
