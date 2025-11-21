from merise_dot.scripts import SQLConversionKernel
from merise_dot.scripts.table import TableFieldType

# some constants
_FOOT = "-- vim"


class MySQLCore(SQLConversionKernel):

    def __init__(self) -> None:
        super().__init__()

    def check_field_type(self, f_type: str) -> TableFieldType:
        ft = f_type.lower()
        if ft == TableFieldType.INTEGER.value:
            return TableFieldType.INTEGER
        elif ft == TableFieldType.BOOLEAN.value:
            return TableFieldType.BOOLEAN
        elif ft == TableFieldType.UUID.value:
            return TableFieldType.UUID
        else:
            super().check_field_type(f_type)

    def __str__(self) -> str:
        return f"{super().__str__()}\n\n{_FOOT}: ft=mysql"
