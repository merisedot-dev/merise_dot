class EntityNotFoundException(Exception):

    def __init__(self, name: str) -> None:
        super().__init__(f"Entity {name} not found")


class LinkDuplicataException(Exception):

    def __init__(self, name: str) -> None:
        super().__init__(f"Link {name} already in graph")


class LinkNotFoundException(Exception):

    def __init__(self, name: str) -> None:
        super().__init__(f"Link {name} not found")
