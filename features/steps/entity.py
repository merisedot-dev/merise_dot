from behave import *
from merise_dot.model.mcd import Entity, entity_parse


@given("an entity named \"{name}\"")
@when("we create a new entity named \"{name}\"")
def make_entity(context, name: str) -> None:
    context.entity = Entity(name)


@given("the entity has {nb:d} fields")
def mk_fields(context, nb: int) -> None:
    for i in range(nb):
        context.entity.add_field(f"field_{i}", "bigint", False)


@given("a field named \"{fname}\"")
def set_field1(context, fname: str) -> None:
    context.e_field1_name = fname


@given("a field with name \"{fname}\" in entity")
def set_field1_in(context, fname: str) -> None:
    context.entity.add_field(fname, "bigint", False)


@given("the field is of type {ftype}")
def set_field1_type(context, ftype: str) -> None:
    context.e_field1_type = ftype


@given("the field is primary ({primary})")
def set_field1_primary(context, primary: str) -> None:
    context.e_field1_primary = primary == "yes"


@when("the field is slotted into the entity")
def slot_field(context) -> None:
    context.entity.add_field(
        context.e_field1_name, context.e_field1_type, context.e_field1_primary)


@when("we delete the field \"{name}\" from the entity")
def field_delete(context, name: str) -> None:
    context.entity.delete_field(name)


@when("we fetch the field \"{name}\" from the entity")
def fetch_field(context, name: str) -> None:
    context.field = context.entity.get_field(name)


@when("we add {nb:d} more fields")
def add_more_fields(context, nb: int) -> None:
    size = len(context.entity._fields)
    for i in range(nb):
        context.entity.add_field(f"field_{i+size}", "bigint", False)


@when("we dump the entity as a string")
def dump_entity(context) -> None:
    context.g_dump = str(context.entity)


@then("the entity's name is \"{name}\"")
def entity_check_name(context, name: str) -> None:
    assert context.entity._name == name


@then("the entity has {nb:d} fields")
def entity_nb_fields(context, nb: int) -> None:
    assert len(context.entity._fields) == nb


@then("the entity has a field named \"{name}\"")
def entity_check_field_name(context, name: str) -> None:
    context.field = context.entity.get_field(name)
    assert context.field


@then("the entity doesn't have a field named \"{name}\"")
def entity_check_not_field_name(context, name: str) -> None:
    try:
        context.entity.get_field(name)
    except:
        pass # it is supposed to crash since there is no such field


@then("the field is of type {ftype}")
def entity_check_field_type(context, ftype: str) -> None:
    (ftype_c, p) = context.field
    assert ftype_c == ftype


@then("the field is primary({prim})")
def entity_check_field_primary(context, prim: str) -> None:
    primary = prim == "yes"
    (f, p) = context.field
    assert primary == p


@then("an entity can be parsed from it")
def check_parse(context) -> None:
    entity_parse(context.json_g_dump)
