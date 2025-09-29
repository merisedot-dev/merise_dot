import questionary
from rich import print as rprint
from merise_dot.model.mcd import Entity


def field_del_op(entity: Entity) -> None:
    f_name: str = questionary.select(
        "Which field do you want to delete ?",
        choices=entity._fields.keys()).ask()
    choice: bool = questionary.confirm(
        f"You wanted to delete the field {f_name}. Are you sure ?").ask()
    if not choice:
        return # no deletion
    entity.delete_field(f_name)
