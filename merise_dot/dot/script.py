from merise_dot.scripts import SQLConversionKernel
from merise_dot.model.mld import MLDGraph
from merise_dot.model.mld.entity import _PK_CODE, _FK_CODE


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
        try:
            for name, ent in graph._entities.items():
                self._core.mk_table(name)
                for f_name, (f_type, st, nl) in ent._fields.items():
                    if st != _FK_CODE:
                        self._core.mk_field(
                            f_name, f_type, st == _PK_CODE or not nl)
                    else:
                        pass # TODO handling foreign keys
                self._core.close_table()
            # TODO transform constraints
            self._script = str(self._core)
        except Exception as e:
            self._script = ""
            raise e

    def __str__(self) -> str:
        if not self._script:
            raise Exception("Cannot find a converted script")
        return self._script
