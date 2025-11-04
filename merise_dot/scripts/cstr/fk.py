from merise_dot.scripts import Constraint


class ForeignKeyConstraintType(Constraint):

    def __init__(self) -> None:
        super().__init__()
        self._pointed: str = ""

    def points_to(self, table: str):
        if not self._pointed:
            self._pointed = table
        return self

    def on_field(self):
        return self
