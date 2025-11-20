from merise_dot.scripts import Constraint


class UniqueConstraint(Constraint):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        # specific constraint info

    def __str__(self) -> str:
        return f""
