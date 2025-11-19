from merise_dot.scripts import SQLConversionKernel
from merise_dot.scripts.mysql import MySQLCore


def choose_core(name: str) -> None:
    if name == "MySQL":
        return MySQLCore()
    else:
        raise Exception("Nonsense")
