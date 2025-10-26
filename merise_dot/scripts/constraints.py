class ConstraintBuilder:
    """Generic constraint maker.
    It's mostly a type thing, extra methods will need to be added on a case by case
    basis.
    """

    def __init__(self, name: str) -> None:
        if type(self) == ConstraintBuilder:
            exit(-1)
        self._name = name
