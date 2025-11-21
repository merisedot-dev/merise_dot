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

    def mk_link(
            self, ent_a: MLDEntity, c_a: int, ent_b: MLDEntity,
            c_b: int) -> None:
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
        if c_a == 1 and c_b == 0:
            pass # TODO
        elif c_a == 0 and c_b == 1:
            pass # TODO
        else:
            raise Exception("Both minimum cardinalities can't be 1")
