class Constraint:
    """Generic constraint maker.
    It's mostly a type thing, extra methods will need to be added on a case by case
    basis.
    """

    def __init__(self, name: str) -> None:
        if type(self) == Constraint:
            exit(-1)
        self._name: str = name
        self._table_name: str = ""

    def set_table(self, name: str):
        """Set which table will have the honor of receiving the constraint.
        It won't check if the table is in database.

        :param name: the table's name.
        :returns: itself to allow for chain programming.
        """
        self._table_name = name
        return self

    def __str__(self) -> str:
        return f"""
            alter table {self._table_name}
                constraint {self._name}
        """
