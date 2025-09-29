import questionary
from rich import print as rprint
from merise_dot.model.mcd import Entity

# modifcation names
_MODS: list[str] = ["change name", "change type", "make primary"]
_PRIMARY_RULES: dict[str | int] = {
    "make primary": 1,
    "make not primary": -1,
    "abort change": 0
}


def edit_field_op(entity: Entity) -> None:
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
        f_t, f_p = entity.get_field(f_name)
        # do the swap
        entity.add_field(n_name, f_t, f_p)
        entity.delete_field(f_name)
    elif mod == _MODS[1]:
        n_type: str = questionary.question("Field's new type :").ask()
        # just raw input for now
        entity.edit_field(f_name, n_type, 0)
    else: # _MODS[2]
        n_pr: int = _PRIMARY_RULES[questionary.select(
            "What to make the field into ?",
            choices=_PRIMARY_RULES.keys()).ask()]
        # do the change
        f_t, _ = entity.get_field(f_name)
        entity.edit_field(f_name, f_t, n_pr)
