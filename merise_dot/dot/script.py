from merise_dot.scripts import SQLConversionKernel
from merise_dot.model.mld import MLDGraph


class Script:

    def __init__(self, core: SQLConversionKernel) -> None:
        """Building our own SQL script from MLD graph.
        The conversion core should be decided first, so it won't cause an issue
        later down the road.

        :param core: the SQL conversion kernel (or core) we'll use in this script
        """
        self._core: SQLConversionKernel = core
        self._script: str = ""

    def mk_sql(self, graph: MLDGraph) -> None:
        """Turn an MLD graph into the SQL script.
        In case of a problem encountered during the conversion, an exception shall
        be thrown and the script progress erased.

        :param graph: the MLD graph used for the conversion.
        """

    def __str__(self) -> str:
        return ""
