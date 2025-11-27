from enum import Enum

from merise_dot.model.mcd import MCDLink


class LinkType:
    """Enumerated class meant to encapsulate how a link is formed
    Enum instances are described as follows :
        - ONE2MANY for (0,n) or (1,n) associations
        - ONE2ONE for (1,1) associations
        - MANY2MANY for (n,n) associations
    """
    ONE2MANY = 1
    ONE2ONE = 2
    MANY2MANY = 3


def mk_lktype(lk: MCDLink) -> LinkType:
    if len(lk._entities) != 2:
        return None # not handled for now
    # parsing cards
    prev: int = None
    for n, (_, m) in lk._entities.items():
        if not prev:
            prev = m
            continue
        # return definition
        if (prev == 1 and m == -1) or (prev == -1 and m == 1):
            return LinkType.ONE2MANY
        elif prev == -1 and m == -1:
            return LinkType.MANY2MANY
        elif prev == 1 and m == 1:
            return LinkType.ONE2ONE
        # weirder situations won't be handled as it doesn't mean anything
    raise Exception("couldn't parse")


def find_direction(lk: MCDLink, t: LinkType) -> (str, str):
    """Fetching link direction.
    This is meant to be only used in a ONE2MANY situation, any other use would
    be nonsensical.

    :param lk: the link entity from an MCD we're fetching from.
    :param t: the link type, just to check...
    :return: the source entity and the destination entity, in this order.
    """
    if t != LinkType.ONE2MANY:
        raise Exception('nonsensical use')
    # parsing cards
    prev: int = None
    p_n: str = None
    for n, (_, m) in lk._entities.items():
        if not prev:
            prev = m
            p_n = n
            continue
        # return zero endpoint
        if prev == 1 and m == -1:
            return (p_n, n)
        elif prev == -1 and m == 1:
            return (n, p_n)
        # weirder situations won't be handled
    raise Exception("couldn't parse")
