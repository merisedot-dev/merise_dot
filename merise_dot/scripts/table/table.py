from .field import TableField


class SQLTable:

    def __init__(self, name: str) -> None:
        self._name: str = name
        # keys are here to avoid duplicatas
        self._fields: dict[str | TableField] = {}

    def add_field(self, field: TableField) -> None:
        if field._name in self._fields.keys():
            raise Exception("Field already in table")
        self._fields[field._name] = field

    def get_pk(self) -> TableField:
        for k, v in self._fields.items():
            if k[0:2] == "pk":
                return v
        return None

    def __str__(self) -> str:
        fields = ",\n\t".join(str(field) for _, field in self._fields.items())
        inner = f"\t{fields}\n" if len(self._fields) > 0 else ""
        return f"create table {self._name} (\n{inner});"
