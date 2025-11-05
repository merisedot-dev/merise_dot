from enum import Enum


class TableFieldType(Enum):
    INTEGER = "int",
    BIGINT = "bigint",
    BOOLEAN = "boolean",
    UUID = "uuid"


class TableField:

    def __init__(self, name: str) -> None:
        self._name: str = name
