class Entity:

    def __init__(self, name: str) -> None:
        self._fields: dict[str | (str, bool)] = {}
        self._name = name

    def add_field(self, name: str, f_type: str, primary: bool) -> None:
        if name in self._fields.keys:
            return # this is supposed to add a field, not overwrite it
        self._fields.update(name, (f_type, primary))

    def __str__(self) -> str:
        return ""
