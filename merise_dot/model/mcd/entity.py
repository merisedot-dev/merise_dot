from .errors import *


class Entity:
    """MCD Entity model.
    This does not take in the concept of foreign keys, as it is irrelevant
    in a Merise MCD schematic.

    For MLD and SQL, we'll use conversion methods, please do use this as
    an MCD wrapper.
    """

    def __init__(self, name: str) -> None:
        self._fields: dict[str | (str, bool)] = {}
        self._name = name

    def add_field(self, f_name: str, f_type: str, primary: bool) -> None:
        """Slotting a new field into an existing entity.
        Keep in mind the name of a field functions as its ID.

        :param f_name: the name of the field. Not case sensitive.
        :param f_type: the type to use for the field.
        :param primary: is the field a primary key for the entity ?

        :raises FieldOverwiteException: if the field already exists.
        """
        name = f_name.lower()
        if name in self._fields.keys():
            raise FieldOverwiteException(f"field {name} already present")
            # this segmentation is for semantics only
        self._fields[name] = (f_type, primary)

    def edit_field(
            self, f_name: str, f_type: str = "", primary: int = 0) -> None:
        """Editing an existing field in an existing entity.
        The field name acts as its ID. As for the values of the primary
        field, please follow this rule :
            - 0 is for "no change"
            - 1 is for "becomes true"
            - -1 is for "becomes false"

        :param f_name: the name of the field. Not case sensitive.
        :param f_type: the type to use for the field.
        :param primary: Is the field to become a primary key or not ?

        :raises FieldNotFoundException: if the field doesn't exist yet.
        """
        name = f_name.lower()
        if not (name in self._fields.keys()):
            raise FieldNotFoundException(f"field {name} not found")
        (f_t, f_p) = self._fields.get(name)
        # swapping info
        f_t = f_t if not f_type else f_type
        f_p = f_p if primary == 0 else True if primary == 1 else False
        self._fields.update(name, (f_t, f_p))

    def get_field(self, f_name: str) -> (str, bool):
        """Fetch field from entity.

        :param f_name:

        :raises FieldNotFoundException:
        """
        name = f_name.lower()
        if not (name in self._fields.keys()):
            raise FieldNotFoundException(f"Field {name} not found")
        return self._fields[name]

    def delete_field(self, f_name: str) -> None:
        """Remove field from an existing Entity.
        The field name acts as its ID. It is not case-sensitive.

        :param f_name: the name of the field to delete.

        :raises FieldNotFoundException: if there is no such field.
        """
        name = f_name.lower()
        if not (name in self._fields.keys()):
            raise FieldNotFoundException(f"field {name} not found")
        self._fields.pop(name)

    def __str__(self) -> str:
        # fields
        fields = ""
        for (k, (t, p)) in self._fields:
            fields += f"""{{
                "name": "{k}",
                "primary": {p},
                "type": "{t}"
                }},"""
        fields[len(fields) - 1] = ""
        # assembling
        return f"""{{
            "name": "{self._name}",
            "fields": {fields}
            }}"""
