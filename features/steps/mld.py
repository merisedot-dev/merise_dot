from behave import *

from merise_dot.model.mcd import Entity


@given("the entity \"{name}\" has {nb:d} fields")
def ensure_mcd_ent_fields(context, name: str, nb: int) -> None:
    entity: Entity = context.graph.get_entity(name)
    for i in range(nb):
        entity.add_field(f"f_{i}", "int", False)


@given("the entity \"{name}\" {status} a primary key")
def ensure_mcd_pk(context, name: str, status: str) -> None:
    st: bool = status.lower() == 'has'
    context.graph.get_entity(name).add_field(f"pk_{name}", "int", True)


@given("the entities \"{n_a}\" and \"{n_b}\" are linked")
def ensure_link_ents(context, n_a: str, n_b: str) -> None:
    pass


@given("the cardinality on \"{name}\" is {c}")
def ensure_lk_card(context, name: str, c: str) -> None:
    pass


@when("we turn the graph into an MLD")
def mk_mld(context) -> None:
    pass


@then("the MLD has an entity named \"{name}\"")
def check_mld_entity(context, name: str) -> None:
    assert False # TODO


@then("the MLD has {nb:d} entities")
def check_mld_nb_ents(context, nb: int) -> None:
    assert False # TODO


@then("the MLD has {nb:d} links")
def check_mld_links(context, nb: int) -> None:
    assert False # TODO


@then("the MLD entity \"{name}\" has {nb:d} fields")
def check_mld_nb_fields(context, name: str, nb: int) -> None:
    assert False # TODO


@then("the MLD entity \"{name}\" {status} a primary key")
def check_mld_pk(context, name: str, status: str) -> None:
    st: bool = status.lower() == 'has'
    assert False # TODO


@then("the entity \"{ent1}\" has a foreign key to \"{ent2}\"")
def check_mld_fk(context, ent1: str, ent2: str) -> None:
    assert False # TODO
