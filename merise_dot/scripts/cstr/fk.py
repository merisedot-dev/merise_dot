from merise_dot.scripts import Constraint


class ForeignKeyConstraintType(Constraint):

    def __init__(self) -> None:
        super().__init__()
        self._pointed: str = ""
        self._origin = None

    def points_to(self, table: str):
        if not self._pointed:
            self._pointed = table
        return self

    def on_field(self):
        return self

    def origin(self, origin: str):
        return self

    def __str__(self) -> str:
        return f"""
            {str(super())}
                foreign key({self._origin})
        """
