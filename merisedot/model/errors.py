# Graph exceptions



class EntityDuplicataException(Exception):

    def __init__(self, name: str) -> None:
        super(f"Entity {name} already in graph")


class EntityNotFoundException(Exception):

    def __init__(self, name: str) -> None:
        super(f"Entity {name} not found")
