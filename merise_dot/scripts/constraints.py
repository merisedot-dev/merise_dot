from .cstr_type import CstrType


class ConstraintBuilder:
    """Generic constraint maker.
    It's mostly a type thing, extra methods will need to be added on a case by case
    basis.
    """

    def __init__(self, name: str) -> None:
        if type(self) == ConstraintBuilder:
            exit(-1)
        self._name: str = name
        self._table_name: str = ""
        # constraint definition fields
        self._c_type: CstrType = None

    def set_table(self, name: str) -> ConstraintBuilder:
        """Set which table will have the honor of receiving the constraint.
        It won't check if the table is in database.

        :param name: the table's name.
        :returns: itself to allow for chain programming.
        """
        self._table_name = name
        return self

    def constraint_type(self, c_type: CstrType) -> ConstraintBuilder:
        """Set what type of constraint we're talking about.
        By "constraint type", we're talking "foreign keys", "unique" or any other
        constraint supported by the implementor SGBD.

        Such constraint management will require the concrete implementorrs to enforce
        some checks about which types are allowed to be used in this method. You'll
        find a provided enum of possible types in this library.

        :param c_type: the constraint's type.
        :returns: itself to allow for chain programming.
        """
        if self._c_type:
            raise Exception("constraint type already set")
        self._c_type = c_type
        return self

    def __str__(self) -> str:
        return f"""
            alter table {self._table_name}
                constraint {self._name}
                {str(self._c_type)}
        """
