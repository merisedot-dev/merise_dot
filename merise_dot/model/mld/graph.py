from .entity import *


class MLDGraph:

    def __init__(self, name: str) -> None:
        self._name: str = name
        self._entities: dict[str | MLDEntity] = {}

    def add_ent(self, name: str) -> None:
        """Adds a new empty entity to the MLD.
        This can't override existing entities.

        :param name: the name and identity of the MLD entity
        """
        if name.lower() in self._entities.keys():
            raise Exception('cannot override')
        ent: MLDEntity = MLDEntity(name.lower())
        self._entities[name.lower()] = ent

    def get_ent(self, name: str) -> MLDEntity:
        """Fetches an entity from an MLD graph.

        :param name: the name and id of the entity to fetch.
        :returns: the entity in the graph, if it exists
        """
        if not name.lower() in self._entities.keys():
            raise Exception('cannot find entity')
        return self._entities[name.lower()]

    def add_ent_field(
            self, name: str, f_name: str, f_t: str, status: int) -> None:
        """Proxy method to add a field to the entity.
        This won't create any new entity in the graph.

        :param name: the name of the new entity we want to add the field in.
        :param f_name: the name of the field to add.
        :param f_t: the type name of the field.
        :param status: determines if the field is a primary, foreign or regular key.
        """
        if not name.lower() in self._entities.keys():
            raise Exception("can't find entity")
        self._entities[name.lower()].add_field(name, f_name, f_t, status)

    def _mk_lkent(self, a: MLDEntity, b: MLDEntity) -> None:
        """Inner method to build intermediate entities.
        The name is determined automatically.

        :param a: first entity of the link
        :param b: second entity of the link
        """
        name = f"lk_{a._name}_{b._name}"
        # building the link
        ent = MLDEntity(name)
        # inner keys
        ent.add_link(a, False)
        ent.add_link(b, False)
        # and into the graph we go
        self._entities[name] = ent

    def mk_link(
        self, ent_a: MLDEntity, c_a: (int, int), ent_b: MLDEntity,
        c_b: (int, int)) -> None:
        """Make a link between two entites in the MLD graph.
        This won't create any new entity unless it's necessary to make the link.

        :param ent_a: the first entity.
        :param c_a: the cardinality on entity A.
        :param ent_b: the second entity.
        :param c_b: the cardinality on entity B.
        """
        if not ent_a._name in self._entities.keys(
        ) or not ent_b._name in self._entities.keys():
            raise Exception('cannot find entities')
        # splitting cards
        min_a, max_a = c_a
        min_b, max_b = c_b
        # parsing cardinalities
        if (min_a == 1 and min_b == 1) or (min_a == 0 and min_b == 0):
            self._mk_lkent(ent_a, ent_b)
        elif min_a == 1 and min_b == 0:
            ent_a.add_link(ent_b)
        elif min_a == 0 and min_b == 1:
            ent_b.add_link(ent_a)
        else:
            raise Exception("Aberrant scenario")
