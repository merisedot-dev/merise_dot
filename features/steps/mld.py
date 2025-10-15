from behave import *

from merise_dot.dot.mkmld import MLDBuilder
from merise_dot.model.mcd import Entity, MCDLink
from merise_dot.model.mld import *


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
    context.lk_name = f"lk_{n_a}_{n_b}"
    context.graph.add_link(context.lk_name, n_a, n_b)


@given("the cardinality on \"{name}\" is {card}")
def ensure_lk_card(context, name: str, card: str) -> None:
    card = card[1:-1]
    min, max = int(card.split(',')[0]), int(
        card.split(',')[1]) if card.split(',')[1] != 'n' else 'n'
    # edit cardinalities
    lk: MCDLink = context.graph.get_link(context.lk_name)
    lk.del_card_str(name)
    lk.add_card(name, min, max)


@when("we turn the graph into an MLD")
def mk_mld(context) -> None:
    mk_mld: MLDBuilder = MLDBuilder()
    mk_mld.mk_mld(context.graph)
    context.mld = mk_mld.get()


@then("the MLD has an entity named \"{name}\"")
def check_mld_entity(context, name: str) -> None:
    assert context.mld.get_ent(name)


@then("the MLD has {nb:d} entities")
def check_mld_nb_ents(context, nb: int) -> None:
    assert len(context.mld._entities) == nb


@then("the MLD has {nb:d} links")
def check_mld_links(context, nb: int) -> None:
    assert False # TODO


@then("the MLD entity \"{name}\" has {nb:d} fields")
def check_mld_nb_fields(context, name: str, nb: int) -> None:
    assert len(context.mld.get_ent(name)._fields) == nb


@then("the MLD entity \"{name}\" {status} a primary key")
def check_mld_pk(context, name: str, status: str) -> None:
    st: bool = status.lower() == 'has'
    ent: MLDEntity = context.mld.get_ent(name)
    for _, (_, prim) in ent._fields.items():
        if st and prim:
            return # found primary key
    if st: # we should have found a primary key
        assert False


@then("the entity \"{ent1}\" has a foreign key to \"{ent2}\"")
def check_mld_fk(context, ent1: str, ent2: str) -> None:
    ent: MLDEntity = context.mld.get_ent(ent1)
    for f_name, (_, st) in ent._fields.items():
        if f_name == f"" and st == _FK_CODE:
            return # found correct fk
    assert False # should have found a key
