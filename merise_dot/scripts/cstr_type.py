class CstrType:
    """Abstract class to handle constraints types.
    This must be derived by each constraint, inner checks included. Please keep in
    mind you'll need to derive the `__str__` method.
    """

    def __init__(self) -> None:
        if type(self) == CstrType:
            exit(-1) # abstract class
