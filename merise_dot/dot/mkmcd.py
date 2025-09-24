from merise_dot.model import Graph
from merise_dot.model.mcd import Entity, MCDLink

# Constants (please do not touch)
EDGE_SETTINGS: str = "edge [\nlen=2\nlabeldistance=2\n];"


class MCDBuilder:

    def __init__(self) -> None:
        # utility attributes
        # output attributes
        self._info: str = ""

    def mk_entity(self, ent: Entity) -> str:

        def frm(f_n: str, f_t: str, f_p: bool) -> str:
            return ""

        return \
        f'''"{ent._name}" [
            shape=record
            label="\\N|{"\l ".join(frm(n, t, p)
                            for n, (t, p) in ent._fields.items)}\l"
        ]'''

    def mk_graph(self, graph: Graph) -> None:
        self._info= \
        f"""graph {graph._name} {{
            {EDGE_SETTINGS}

            {"\n\n".join(self.mk_entity(ent)
                    for _, ent in graph._entities.items())}
        }}"""
