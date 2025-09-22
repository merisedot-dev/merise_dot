# Field exceptions


class FieldOverwiteException(Exception):

    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class FieldNotFoundException(Exception):

    def __init__(self, msg: str) -> None:
        super().__init__(msg)


# Link exceptions


class LinkOverwriteException(Exception):

    def __init__(self, name: str) -> None:
        super().__init__(f"Link to {name} not found")
