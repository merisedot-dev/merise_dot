from merise_dot.scripts import SQLConversionKernel
from merise_dot.scripts.cstr import ForeignKeyConstraint, UniqueConstraint

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

    def mk_fks(self, graph: MLDGraph) -> None:
        for name, ent in graph._entities.items():
            for f_name, (_, st, nl) in ent._fields.items():
                if st != _FK_CODE:
                    continue # nothing useful here
                subname = f_name[3:len(f_name)]
                dest = self._core.get_table(subname) # FIXME
                cst = ForeignKeyConstraint(f"fk_{name}_{subname}")
                # constraint contents
                cst.set_table(name).origin(
                    self._core.get_table(name)._fields[f_name]).points_to(
                        dest).on_field(dest.get_pk())
                # adding constraint to the conversion core
                self._core.mk_constraint(cst)

    def mk_sql(self, graph: MLDGraph) -> None:
        """Turn an MLD graph into the SQL script.
        In case of a problem encountered during the conversion, an exception shall
        be thrown and the script progress erased.

        :param graph: the MLD graph used for the conversion.
        """
        try:
            self._core.db_name(graph._name)
            for name, ent in graph._entities.items():
                # entity transformations
                self._core.mk_table(name)
                for f_name, (f_type, st, nl) in ent._fields.items():
                    self._core.mk_field(
                        f_name, f_type, st == _PK_CODE or not nl,
                        st == _PK_CODE)
                    # foreign keys on second pass
                # transform constraints
                # intermediate tables
                if name[0:2] == "lk":
                    cst = UniqueConstraint(f"unq_{name}")
                    cst.set_table(name)
                    for _, sf in self._core._current_table._fields.items():
                        cst.add_field(sf)
                    self._core.mk_constraint(cst)

                # second pass for foreign keys
                self.mk_fks(graph)

                # writing script
                self._core.close_table()
        # transform script into str
            self._script = str(self._core)
        except Exception as e:
            self._script = ""
            raise e

    def __str__(self) -> str:
        if not self._script:
            raise Exception("Cannot find a converted script")
        return self._script
