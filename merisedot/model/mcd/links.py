from .errors import LinkOverwriteException
from .entity import Entity


class MCDLink:

    def __init__(self, name: str) -> None:
        self._name = name
        # moving parts
        self._entities: dict[str | (int, int)] = {}

    def add_card(self, entity: Entity, min: int, max: int) -> None:
        """Add cardinalities to link entity.

        :param entity:
        :param min:
        :param max:
        """
        if entity._name in self._entities.keys():
            return # silent fail
        self._entities[entity._name] = (min, max)

    def __str__(self) -> str:
        # cardinalities
        cards = "["
        for (k, (v1, v2)) in self._entities:
            cards += f"\"{k}\": [ {v1}, {v2} ]"
        cards[len(cards) - 1] = "]"
        # assembling
        return f"""{{
            "name": "{self._name}",
            "entities": {cards}
            }}"""
