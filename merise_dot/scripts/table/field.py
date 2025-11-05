from .tft import *


class TableField:

    def __init__(self, name: str, tf_type: TableFieldType) -> None:
        self._name: str = name
        self._tf_type: TableFieldType = tf_type
        # extra field information
        self._default_val: any = None

    def pk(self) -> None:
        pass

    def nullable(self, null: bool = True) -> None:
        pass

    def ensure_default(self) -> None:
        pass
