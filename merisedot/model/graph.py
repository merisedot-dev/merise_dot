from .mcd import Entity


class Graph:
    # TODO write attributes

    def __init__(self) -> None:
        self._contents: str = ""
        # MCD specifics
        self._entities: dict[str | Entity] = {}
        # TODO add links

    def parse(self, contents: str) -> None:
        pass # TODO

    def add_entity(self, name: str) -> Entity:
        pass # TODO

    def add_link(self, e_a: str, e_b: str) -> None:
        pass # TODO
