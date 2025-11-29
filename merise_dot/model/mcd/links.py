from .errors import LinkOverwriteException
from .entity import Entity


class MCDLink:

    def __init__(self, name: str) -> None:
        self._name = name
        # moving parts
        self._entities: dict[str | (int, int)] = {}
        self._fields: dict[str | str] = {}

    def add_card(self, entity: Entity, min: int, max: int) -> None:
        """Add cardinalities to link entity.

        :param entity: the other MCD entity to link.
        :param min: the minimum cardinality of the link (mostly 0 or 1).
        :param max: the max cardinality (-1 is "n").
        """
        self.add_card_str(entity._name, min, max)

    def add_card_str(self, entity: str, min: int, max: int) -> None:
        """Add cardinalities to link entity.
        This is the from_string variant of `MCDLink.add_card`.

        :param entity: the name of the linked entity.
        :param min: the minimum cardinality (usually 0 or 1).
        :param max: the max cardinality (1 or -1 for "n").
        """
        if entity in self._entities.keys():
            return # silent fail
        self._entities[entity] = (min, max)

    def del_card_str(self, card: str) -> None:
        """Removes an entity from the link.
        In case of unknown entity, this will just silently fail.

        :param card: the name of the linked entity.
        """
        if not (card in self._entities.keys()):
            return # silent fail
        self._entities.pop(card)

    def get_card(self, card: str) -> (int, int):
        """Fetches the inner data for a linked entity.
        For an MCD, we'll only care about the cardinality values. In case of an
        unknown entity, this will silently fail.

        :returns: a tuple (min,max) for the given entity.
        """
        if not (card in self._entities.keys()):
            return None
        return self._entities[card.lower()]

    def edit_card(self, entity: Entity, c_min: int, c_max: int) -> None:
        """Swap cardinality info.
        This will only work for known entities, otherwise you will get an exception
        thrown your way.

        :param entity: the MCD entity we want to tweak.
        :param c_min: the minimum cardinality (0 or 1)
        :param c_max: the max cardinality (-1 is still "n")
        """
        if not entity._name in self._entities.keys():
            raise Exception('cannot edit unknown cardinality')
        self._entities[entity._name] = (c_min, c_max)

    def add_field(self, f_name: str, f_type: str) -> None:
        if f_name.lower() in self._fields.keys():
            raise Exception()
        self._fields[f_name.lower()] = f_type.lower()

    def get_field(self, f_name: str) -> str:
        if not f_name.lower() in self._fields.keys():
            raise Exception()
        return self._fields[f_name.lower()]

    def del_field(self, f_name: str) -> None:
        if not f_name.lower() in self._fields.keys():
            raise Exception()
        self._fields.pop(f_name.lower())

    def edit_field(self, f_name: str, f_type: str) -> None:
        if not f_name.lower() in self._fields.keys():
            raise Exception('field not found')
        self._fields[f_name.lower()] = f_type

    def __str__(self) -> str:
        return f"""{{
            "name": "{self._name}",
            "entities": {{
                {",".join(f'"{k}": [{v1},{v2}]'
                    for k, (v1, v2) in self._entities.items())}
                }},
            "fields": {{
                {",".join(f'"{k}": "{v}"' for k, v in self._fields.items())}
                }}
            }}"""


def link_parse(info: dict) -> MCDLink:
    lk = MCDLink(info["name"])
    for ent, cards in info["entities"].items():
        lk.add_card_str(ent, cards[0], cards[1])
    for k, v in info["fields"].items():
        lk.add_field(k, v)
    return lk
