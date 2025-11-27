from .lkt import *

from merise_dot.model import MCDGraph
from merise_dot.model.mcd import Entity, MCDLink
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
                f_name, f_type, _PK_CODE if prim else _REGULAR_CODE) # FIXME

    def _mk_one2many(self, graph: MCDGraph, link: MCDLink) -> None:
        """Inner builder for ONE2MANY link scenarios.
        This is meant to simplify how we build such things into the MLD graph.
        It does not return anything and isn't meant to be called by anything other
        than its own class.

        :param graph: the MCD graph we're fetching extra data from.
        :param link: the link entity we're dealing wth.
        """
        src, dst = find_direction(link, LinkType.ONE2MANY)
        # fetching cardinalities
        n_src, _ = link.get_card(src)
        # fetching entities
        ent_src: MLDEntity = self._graph.get_ent(src)
        ent_dst: MLDEntity = self._graph.get_ent(dst)
        # adding corresponding foreign keys
        ent_src.add_link(ent_dst, n_src == 0)

    def _mk_many2many(self, graph: MCDGraph, link: MCDLink) -> None:
        """Inner builder for MANY2MANY situations.
        This doesn't create any nonlink entity in the MLD graph.

        :param graph: the MCD graph we're fetching extra data from.
        :param link: the link entity we're dealing with.
        """
        self._graph.add_ent(link._name)
        ent: MLDEntity = self._graph.get_ent(link._name)
        # add foreign keys to link entity
        for name, _ in link._entities.items():
            ent.add_link(self._graph.get_ent(name), False)
        # adding extra fields
        for name, (ft, nl) in link._fields.items():
            ent.add_field(name, ft, _REGULAR_CODE, nl)

    def mk_mld(self, graph: MCDGraph) -> None:
        """Turn an MCD graph into an MLD one.
        We're not checking if the graph is well formed, as inner methods from the
        MCD graph should already have kicked in and crashed out.

        :param graph: the graph to convert.
        """
        self._name = graph._name
        try:
            # basic setup
            self._graph = MLDGraph(self._name)
            # slotting entities into the MLD
            for _, ent in graph._entities.items():
                self._mk_ent(ent) # building base entity
            # Entities links conversion
            for _, lk in graph._links.items():
                lt: LinkType = mk_lktype(lk)
                # deciding what to do with the link
                if lt == LinkType.ONE2MANY:
                    self._mk_one2many(graph, lk)
                elif lt == LinkType.MANY2MANY:
                    self._mk_many2many(graph, lk)
        except Exception as e:
            self._graph = None
            raise e

    def get(self) -> MLDGraph:
        """Fetched the transformed graph.

        :returns: The processed MLD graph. None if no processing occured.
        """
        return self._graph
