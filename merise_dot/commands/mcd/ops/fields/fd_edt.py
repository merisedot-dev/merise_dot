import questionary
from rich import print as rprint
from merise_dot.model.mcd import Entity
from merise_dot.dot import mkrt

# modifcation names
_MODS: list[str] = ["change name", "change type", "make primary"]


def edit_field_op(entity: Entity) -> None:
    rprint(mkrt(entity))
    f_name: str = questionary.select(
        "Choose a field to edit", choices=entity._fields.keys()).ask()
    # choose modification
    mod: str = questionary.select(
        "What to do with this field ?", choices=_MODS).ask()
    # apply modification
    if mod == _MODS[0]:
        n_name: str = questionary.question("Field's new name :").ask()
        if n_name in entity._fields.keys():
            rprint(f"Another field is already named {n_name}")
            return
    elif mod == _MODS[1]:
        n_type: str = questionary.question("Field's new type :").ask()
        # TODO sanitize
