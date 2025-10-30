from .constraints import *


class SQLConversionKernel:
    """Core of the MLD to SQL conversion process.
    This will ensure flexibility for the conversion process, but it won't perform
    any writing on its own.
    """

    def __init__(self) -> None:
        if type(self) == SQLConversionKernel:
            exit(-1) # this is abstract
        self._current_table = None

    def mk_table(self, name: str) -> None:
        """Add a new table to write into into the script.

        :param name: The table's name. Must be unique.
        """

    def close_table(self) -> None:
        """Close the table we're writing into.
        """
        self._current_table = None

    def mk_field(self, name: str, f_type: str, nullable: bool = True) -> None:
        """Add a field into the current table we're editing.

        :param name: The field's name.
        :param f_type: The field's type (pre-check)
        :param nullable: Wether the field can be null or not.
        """

    def mk_constraint(self, cstr: ConstraintBuilder) -> None:
        """Define a constraint for the table we're editing.

        :param cstr: The constraint builder to check the definition of said
        constraint.
        """
