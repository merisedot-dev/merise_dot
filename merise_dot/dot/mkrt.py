from rich.table import Table
from merise_dot.model.mcd import Entity, MCDLink


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


def mk_link_richtable(link: MCDLink) -> Table:
    t = Table(title=link._name)
    # column setup
    t.add_column("Entity")
    t.add_column("minimum")
    t.add_column("maximum")
    # adding fields
    for e_name, (e_min, e_max) in link._entities.items():
        t.add_row(e_name, e_min, "n" if e_max == -1 else e_max)
    return t
