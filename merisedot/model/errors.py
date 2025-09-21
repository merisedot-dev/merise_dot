# Field exceptions


class FieldOverwiteException(Exception):

    def __init__(self, msg: str) -> None:
        super(msg)


class FieldNotFoundException(Exception):

    def __init__(self, msg: str) -> None:
        super(msg)


# Graph exceptions


class EntityDuplicataException(Exception):

    def __init__(self, name: str) -> None:
        super(f"Entity {name} already in graph")


class EntityNotFoundException(Exception):

    def __init__(self, name: str) -> None:
        super(f"Entity {name} not found")
