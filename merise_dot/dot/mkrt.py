from rich.table import Table
from merise_dot.model.mcd import Entity


def mk_entity_richtable(entity: Entity) -> Table:
    t = Table(title=entity._name)
    # column setup
    t.add_column("Primary", style="bold")
    t.add_column("Field name")
    t.add_column("Field type")
    # adding fields
    for f_n, (f_t, f_p) in entity._fields.items():
        p = "PK" if f_p else ""
        t.add_row(p, f_n, f_p)
    return t
