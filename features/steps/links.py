from behave import *
from merise_dot.model.mcd import MCDLink


@given("a link named \"{name}\"")
@when("we create a link named \"{name}\"")
def mk_link(context, name: str) -> None:
    context.lk = MCDLink(name)


@given("the link has {nb:d} cardinalities")
def ensure_cardis(context, nb: int) -> None:
    for i in range(nb):
        context.lk.add_card_str(f"e_{i}", 0, -1)


@when("we remove {nb:d} cardinalities from link")
def rm_cardis(context, nb: int) -> None:
    for i in range(nb):
        context.lk.del_card_str(f"e_{i}")


@when("we add a field named \"{name}\" with type {f_t} to the link")
def add_link_field(context, name: str, f_t: str) -> None:
    context.lk_field_name: str = name
    context.lk.add_field(name, f_t)


@then("the link has no cardinalities")
def check_no_card(context) -> None:
    assert len(context.lk._entities) == 0


@then("the link has {nb:d} cardinalities")
def check_nb_cards(context, nb: int) -> None:
    assert len(context.lk._entities) == nb


@then("one cardinality of the link points to \"{dst}\"")
def check_lk_points(context, dst: str) -> None:
    assert context.lk.get_card(dst)


@then("the link has {nb:d} field(s)")
def check_nb_link_fields(context, nb: int) -> None:
    assert len(context.lk._fields) == nb


@then("the link field is named \"{name}\"")
def check_link_field_name(context, name: str) -> None:
    assert context.lk.get_field(name)


@then("the link field is of type {f_t}")
def check_link_field_type(context, f_t: str) -> None:
    assert context.lk.get_field(context.lk_field_name) == f_t
