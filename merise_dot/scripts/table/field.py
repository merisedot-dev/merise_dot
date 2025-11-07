from .tft import *


class TableField:

    def __init__(self, name: str, tf_type: TableFieldType) -> None:
        self._name: str = name
        self._tf_type: TableFieldType = tf_type
        # extra field information
        self._default: any = None # just a failsafe
        self._is_pk: bool = False
        self._nullable: bool = True

    def pk(self) -> None:
        self._is_pk = True

    def nullable(self, null: bool = True) -> None:
        self._nullable = null

    def ensure_default(self) -> None:
        self._default = tft_default(self._tf_type)

    def __str__(self) -> None:
        kind = "primary key" if self._is_pk else ""
        nla = "not null" if not self._nullable else ""
        return f"{self._name} {self._tf_type} {kind} {nla}"
