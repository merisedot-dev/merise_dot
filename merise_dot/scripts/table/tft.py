from enum import Enum
from uuid import UUID


class TableFieldType(Enum):
    INTEGER = "int",
    BIGINT = "bigint",
    BOOLEAN = "boolean",
    UUID = "uuid"


def tft_default(tft: TableFieldType) -> any:
    if tft in [tft.INTEGER, tft.BIGINT]:
        return 0 # int defaults
    elif tft == tft.BOOLEAN:
        return False # most safe boolean option
    elif tft == tft.UUID:
        return UUID(int=0) # nil UUID, another safe option
    # TODO fetch other types
    else:
        return None
