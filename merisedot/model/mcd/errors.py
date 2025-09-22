# Field exceptions


class FieldOverwiteException(Exception):

    def __init__(self, msg: str) -> None:
        super(msg)


class FieldNotFoundException(Exception):

    def __init__(self, msg: str) -> None:
        super(msg)


# Link exceptions


class LinkOverwriteException(Exception):

    def __init__(self, name: str) -> None:
        super(f"Link to {name} not found")
