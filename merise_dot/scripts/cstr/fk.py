from merise_dot.scripts import Constraint
from merise_dot.scripts.table import SQLTable, TableField, TableFieldType


class ForeignKeyConstraint(Constraint):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        # pointed table info
        self._pointed: SQLTable = None
        self._on: TableField = None
        # source table info
        self._origin: TableField = None

    def points_to(self, table: SQLTable):
        if self._pointed:
            raise Exception("pointed table already set")
        self._pointed = table
        return self

    def on_field(self, f_name: str):
        if not self._pointed:
            raise Exception("unknown table to point to")
        self._on = self._pointed._fields[f_name]
        return self

    def origin(self, origin: TableField):
        if self._origin:
            raise Exception("origin already set")
        self._origin = origin
        return self

    def __str__(self) -> str:
        # assembling basic info
        ref = f"{self._pointed._name}.{self._on._name}"
        text: str = f"foreign key({self._origin._name})\n\t\t\treferences {ref}"
        # formatting output
        return f"{super().__str__()}\n\t\t{text};"
