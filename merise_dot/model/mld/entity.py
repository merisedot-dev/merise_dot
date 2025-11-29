# Extra constants, please do not touch
_REGULAR_CODE: int = 0
_PK_CODE: int = 1
_FK_CODE: int = 2


class MLDEntity:
    """MLD_specific overlay on the old MCD Entity.
    This is meant to provide a unified interface for the old types, now that the
    user wants MLD conversion.

    MCD should remain the main way for a user to interact with a database graph.
    """

    def __init__(self, name: str) -> None:
        self._name: str = name
        self._fields: dict[str | (str, int, bool)] = {}
        self._links: dict[str | str] = {}

    def add_field(
            self,
            name: str,
            f_type: str,
            status: int = _REGULAR_CODE,
            nullable: bool = False) -> None:
        """Adding a new field to the entity.

        :param name: the field's name.
        :param f_type: the type of the field we want to add.
        :param status: the status of the field, a regular one by default.
        :param nullable: wether the field can be null or not.
        """
        if name.lower() in self._fields.keys():
            raise Exception('field already exists')
        self._fields[name.lower()] = (
            f_type, status, False if status == _PK_CODE else nullable)

    def get_pk(self) -> (str, int):
        """Fetches the primary key information of the entity.
        As it is a primary key, we will not check if it can be null. It cannot be.

        :returns: a tuple made of the type name and key status for further checks.
        """
        for _, (t, st, _) in self._fields.items():
            if st == _PK_CODE:
                return (t, st)
        raise Exception('no PK')

    def add_link(self, other, nullable: bool = True) -> None:
        """Link builder abstraction for entities link.
        It won't create extra entities, but it will edit existing ones to add
        extra fields.

        :param other: the oher entity in the link.
        :param nullable: wether the link can be broken or not;
        """
        if type(other) != MLDEntity:
            raise Exception("WTF")
        name: str = f"fk_{other._name}"
        ft, _ = other.get_pk()
        self.add_field(name, ft, _FK_CODE, nullable)
        self._links[name] = other._name
