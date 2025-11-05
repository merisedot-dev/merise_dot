from .field import TableField


class SQLTable:

    def __init__(self, name: str) -> None:
        self._name: str = name
        # keys are here to avoid duplicatas
        self._fields: dict[str | TableField] = []

    def add_field(self, field: TableField) -> None:
        pass
