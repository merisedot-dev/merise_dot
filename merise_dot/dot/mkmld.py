from .lkt import *

from merise_dot.model import Graph
from merise_dot.model.mcd import Entity
from merise_dot.model.mld import MLDGraph
from merise_dot.model.mld.entity import *


class MLDBuilder:

    def __init__(self) -> None:
        self._name: str = ""
        self._graph: MLDGraph = None

    def _mk_ent(self, ent: Entity) -> None:
        """Inner method for entity generation.
        This is only a basic transformation, the link generation should be the
        main chokepoint of the MLD conversion.

        :param ent: the MCD entity to transform
        """
        self._graph.add_ent(ent._name)
        mld_ent: MLDEntity = self._graph.get_ent(ent._name)
        for f_name, (f_type, prim) in ent._fields.items():
            mld_ent.add_field(
                f_name, f_type, _PK_CODE if prim else _REGULAR_CODE)

    def mk_mld(self, graph: Graph) -> None:
        """Turn an MCD graph into an MLD one.
        We're not checking if the graph is well formed, as inner methods from the
        MCD graph should already have kicked in and crashed out.

        :param graph: the graph to convert.
        """
        self._name = graph._name
        try:
            self._graph = MLDGraph(self._name)
            for _, ent in graph._entities.items():
                self._mk_ent(ent) # building base entity

            for _, lk in graph._links.items():
                t: LinkType = mk_lktype(lk)
                if t == LinkType.MANY2MANY:
                    lkn: str = f"lk_{"_".join(n for n in lk._cardinalities.keys())}"
                    self._graph.add_ent(lkn)
                    # add foreign keys
                    ent: MLDEntity = self._graph.get_ent(lkn)
                    for n, _ in lk._cardinalities.items():
                        lkd: MLDEntity = self._graph.get_ent(n)
                        t,_=lkd.get_pk()
                        ent.add_field(f"{n}", t, _FK_CODE)
                # TODO other cases
        except Exception as e:
            self._graph = None

    def get(self) -> MLDGraph:
        """Fetched the transformed graph.

        :returns: The processed MLD graph. None if no processing occured.
        """
        return self._graph
