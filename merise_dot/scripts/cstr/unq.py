from merise_dot.scripts import Constraint
from merise_dot.scripts.table import TableField


class UniqueConstraint(Constraint):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        # specific constraint info
        self._fields: dict[str | TableField] = {}

    def add_field(self, field: TableField) -> None:
        if field._name in self._fields.keys():
            raise Exception("duplicate field")
        self._fields[field._name] = field

    def __str__(self) -> str:
        if len(self._fields) == 0:
            raise Exception("You are supposed to make some fields unique")
        # assembling text
        text = f"unique ({", ".join(n for n in self._fields.keys())});"
        # formatting output
        return f"{super().__str__()}\n\t\t{text}"
