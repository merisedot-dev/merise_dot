from .errors import LinkOverwriteException
from .entity import Entity


class MCDLink:

    def __init__(self, name: str) -> None:
        self._name = name
        # moving parts
        self._entities: dict[str | (int, int)] = {}
        self._fields: dict[str | str] = {}

    def add_card(self, entity: Entity, min: int, max: int) -> None:
        self.add_card_str(entity._name, min, max)

    def add_card_str(self, entity: str, min: int, max: int) -> None:
        """Add cardinalities to link entity.

        :param entity:
        :param min:
        :param max:
        """
        if entity in self._entities.keys():
            return # silent fail
        self._entities[entity] = (min, max)

    def del_card_str(self, card: str) -> None:
        if not (card in self._entities.keys()):
            return # silent fail
        self._entities.pop(card)

    def get_card(self, card: str) -> (int, int):
        if not (card in self._entities.keys()):
            return None
        return self._entities[card.lower()]

    def edit_card(self, entity: Entity, c_min: int, c_max: int) -> None:
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
