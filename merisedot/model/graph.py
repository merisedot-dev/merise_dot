from .mcd import Entity
from .errors import *


class Graph:
    """Merise database graph.
    This is a MCD-compliant graph only as of now, conversions will be done
    later on.
    """

    def __init__(self, name: str) -> None:
        self._name = name
        # MCD specifics
        self._entities: dict[str | Entity] = {}
        # TODO add links

    def parse(self, contents: str) -> None:
        pass # TODO

    def add_entity(self, e_name: str) -> Entity:
        """Create a new entity in the graph. Links not included.
        The name of an Entity will serve as its ID. Not case-sensitive.

        :param e_name: the entity's name.
        :returns: the newly formed Entity.

        :raises EntityDuplicataException: if the entity is already there.
        """
        name = e_name.lower()
        if name in self._entities.keys():
            raise EntityDuplicataException(name)
        entity = Entity(name)
        self._entities.update(name, entity)
        return entity

    def del_entity(self, e_name: str) -> None:
        """Removes an entity from graph.
        It also removes every link it has from graph. Entity's name also
        acts like an ID. Not case-sensitive.

        :param e_name: the name of the entity.

        :raises EntityNotFoundException: if no entity was found.
        """
        name = e_name.lower()
        if not (name in self._entities.keys()):
            raise EntityNotFoundException(name)
        self._entities.pop(name)

    def __str__(self) -> str:
        # entities
        entities = "["
        for (_, e) in self._entities:
            entities += f"{str(e)},"
        entities[len(entities) - 1] = "]"
        # links
        # TODO
        # assembling
        return f"""{{
            "name": "{self._name}",
            "entities": {entities}
            }}"""
