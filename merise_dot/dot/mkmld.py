from .lkt import *

from merise_dot.model import Graph
from merise_dot.model.mcd import Entity
from merise_dot.model.mld import MLDGraph
from merise_dot.model.mld.entity import *

# extra key constants
_REGULAR_CODE: int = 0
_PK_CODE: int = 1
_FK_CODE: int = 2


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
                    lkn: str = f"lk_{"_".join(n for n in lk._entities.keys())}"
                    self._graph.add_ent(lkn)
                    # add foreign keys
                    ent: MLDEntity = self._graph.get_ent(lkn)
                    for n, (_, _) in lk._entities.items():
                        lkd: MLDEntity = self._graph.get_ent(n)
                        ent.add_field(f"fk_{n}", lkd.get_pk()[0], _FK_CODE)
                    # add extra attributes
                    for n, (t, _) in lk._fields.items():
                        ent.add_field(n, t)

                elif t == LinkType.ONE2ONE:
                    c0: str = list(lk._entities.keys())[0]
                    c1: str = list(lk._entities.keys())[1]
                    # find entities
                    ent0: MLDEntity = self._graph.get_ent(c0)
                    ent1: MLDEntity = self._graph.get_ent(c1)
                    # add foreign keys
                    ent0.add_field(f"fk_{c1}", ent1.get_pk()[0], _FK_CODE)
                    ent1.add_field(f"fk_{c0}", ent0.get_pk()[0], _FK_CODE)

                elif t == LinkType.ONE2MANY:
                    dir, other = find_direction(lk, t)
                    # getting entities
                    ent: MLDEntity = self._graph.get_ent(dir)
                    o_ent: MLDEntity = self._graph.get_ent(other)
                    # adding foreign key field
                    ent.add_field(f"fk_{other}", o_ent.get_pk()[0], _FK_CODE)
        except Exception as e:
            self._graph = None
            raise e

    def get(self) -> MLDGraph:
        """Fetched the transformed graph.

        :returns: The processed MLD graph. None if no processing occured.
        """
        return self._graph
