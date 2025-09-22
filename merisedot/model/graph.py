from .mcd import Entity, MCDLink
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
        self._links: dict[str | MCDLink] = {}

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
        self._entities[name] = entity
        return entity

    def get_entity(self, e_name: str) -> Entity:
        name = e_name.lower()
        if not (name in self._entities.keys()):
            raise EntityNotFoundException(name)
        return self._entities[name]

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

    def add_link(self, l_name: str, ea: str, eb: str) -> None:
        """Add a link between two entities on graph.
        Link name acts as id. Not case-sensitive.

        :param l_name: the name of the link to create.
        :param ea: the name of the first entity linked.
        :param eb: the name of the second entity linked.
        """
        name = l_name.lower()
        if name in self._links.keys():
            raise LinkDuplicataException(name)
        link = MCDLink(name)
        link.add_card(self.get_entity(ea), 0, -1)
        link.add_card(self.get_entity(eb), 0, -1)
        self._links[name] = link

    def __str__(self) -> str:
        # entities
        entities = "["
        for (_, e) in self._entities:
            entities += f"{str(e)},"
        entities[len(entities) - 1] = "]"
        # links
        links = "["
        for (_, l) in self._links:
            links += f"{str(l)},"
        links[len(links) - 1] = "]"
        # assembling
        return f"""{{
            "name": "{self._name}",
            "entities": {entities},
            "links: {links}
            }}"""
