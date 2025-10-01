import questionary
from rich import print as rprint
from merise_dot.model.mcd import Entity, FieldOverwiteException
from merise_dot.dot import mkrt


def add_field_op(entity: Entity) -> None:
    rprint(mkrt(entity))
    f_name: str = questionary.text("Field name :").ask()
    f_type: str = questionary.text("Field type :").ask()
    f_pr: bool = questionary.confirm("Make field primary ?").ask()
    # slotting field in entity
    try:
        entity.add_field(f_name, f_type, f_pr)
    except FieldOverwiteException as e:
        rprint(f"Couldn't insert field : {e}")
