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
    if status.lower() == 'has':
        context.graph.get_entity(name).add_field(f"pk_{name}", "int", True)


@given("the entities \"{n_a}\" and \"{n_b}\" are linked")
def ensure_link_ents(context, n_a: str, n_b: str) -> None:
    context.lk_name = f"lk_{n_a}_{n_b}"
    context.graph.add_link(context.lk_name, n_a, n_b)


@given("the cardinality on \"{name}\" is ({min:d},{max})")
def ensure_lk_card(context, name: str, min: int, max: str) -> None:
    max_card: int = -1 if max == 'n' else int(max)
    # edit cardinalities
    lk: MCDLink = context.graph.get_link(context.lk_name)
    lk.del_card_str(name)
    lk.add_card_str(name, min, max_card)


@given("\"{ent1}\" is linked to \"{ent2}\" by the cardinality ({n:d},{m})")
def mld_mkfk(context, ent1: str, ent2: str, n: int, m: str) -> None:
    # filtering constants
    maxi = -1 if m == "n" else int(m)
    lkname = f"lk_{min(ent1, ent2)}_{max(ent1, ent2)}"
    # actual test
    try: # link does exist
        lk: MCDLink = context.graph.get_link(lkname) # FIXME
        lk.edit_card(context.graph.get_entity(ent1), n, maxi)
    except: # link does not exist
        context.graph.add_link(lkname, ent1, ent2)
        lk: MCDLink = context.graph.get_link(lkname)
        lk.edit_card(context.graph.get_entity(ent1), n, maxi)


@given("the graph is turned into an MLD")
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
    seen: int = 0
    for _, ent in context.mld._entities.items():
        for _, (_, st, nl) in ent._fields.items():
            if st == 3: # Found a foreign key
                seen += 1
                if seen > nb:
                    assert False # no need to continue
    assert seen == nb


@then("the MLD entity \"{name}\" has {nb:d} fields")
def check_mld_nb_fields(context, name: str, nb: int) -> None:
    assert len(context.mld.get_ent(name)._fields) == nb


@then("the MLD entity \"{name}\" {status} a primary key")
def check_mld_pk(context, name: str, status: str) -> None:
    st: bool = status.lower() == 'has'
    ent: MLDEntity = context.mld.get_ent(name)
    try:
        ent.get_pk() # PK check
    except Exception as e:
        if st: # if there shouldn't be one, everything is fine
            assert False # something should have happened


@then("the entity \"{ent1}\" has a foreign key to \"{ent2}\" (yes)")
@then("the entity \"{ent1}\" has a foreign key to \"{ent2}\"")
def check_mld_fk(context, ent1: str, ent2: str) -> None:
    context.no_fk = False
    ent: MLDEntity = context.mld.get_ent(ent1)
    for f_name, (ft, st, nl) in ent._fields.items():
        if f_name == f"fk_{ent2}" and st == 2: # 2 if FK code
            context.fk = (ft, st, nl) # saving foreign key for later
            return # found correct fk
    assert False # should have found a key


@then("the entity \"{ent1}\" has a foreign key to \"{ent2}\" (no)")
def mld_no_fk(context, ent1: str, ent2: str) -> None:
    context.no_fk = True
    ent: MLDEntity = context.mld.get_ent(ent1)
    for fn, (ft, st, nl) in ent._fields.items():
        if fn == f"fk_{ent2}" and st == 2: # 2 is FK code
            assert False # this should not be here


@then("this field is nullable (yes)")
def mld_nlfk(context) -> None:
    if context.no_fk:
        return
    _, _, nl = context.fk # splitting back tuple
    assert nl


@then("this field is nullable (no)")
def mld_nonlfk(context) -> None:
    if context.no_fk:
        return
    _, _, nl = context.fk
    assert not nl
