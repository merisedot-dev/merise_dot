import json
from .mcd import Entity, MCDLink, entity_parse, link_parse
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
        for _, link in self._links.items():
            link.del_card_str(name)

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

    def get_link(self, l_name: str) -> MCDLink:
        if not (l_name in self._links.keys()):
            raise Exception(f"not found {l_name}")
        return self._links[l_name]

    def __str__(self) -> str:
        return f"""{{
            "name": "{self._name}",
            "entities": [{",".join(
                [str(e) for (k,e) in self._entities.items()])}],
            "links": [{",".join(
                [str(l) for (k,l) in self._links.items()])}]
            }}"""


def graph_parse(info: str) -> Graph:
    """Parsing a new graph from a file's content.

    :param info:
    """
    json_info = json.loads(info)
    g = Graph(json_info["name"])
    # adding entities
    for entity in json_info["entities"]:
        en = entity_parse(entity)
        g._entities[en._name] = en
    # adding links
    for link in json_info["links"]:
        lk = link_parse(link)
        g._links[lk._name] = lk
    return g
