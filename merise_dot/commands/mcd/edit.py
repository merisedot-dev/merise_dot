import os, pzp
from rich import print as rprint

# inner imports
from merise_dot.model import Graph
from .ops import *


# smol ops hack to ensure we can exit the normal way
def merise_exit(graph: Graph) -> None:
    rprint("Exiting...")
    exit(0)


# constants, please do not touch
_OPS = {
    "add an entity": add_entity_op,
    "edit an entity": edit_entity_op,
    "delete an entity": del_entity_op,
    "link two entities": link_entity_op,
    "exit": merise_exit
}


def edit_graph(graph: Graph, path: str) -> None:
    while True: # it's a mainloop
        rprint("[bold] Choose an operation to perform : ", end="")
        qst: str = pzp.pzp(_OPS.keys(), fullscreen=False, height=7)
        _OPS[qst](graph)
        # save graph to file before losing it
        sv_proc = os.fork()
        if sv_proc == 0: # we're in subprocess
            with open(path, 'w') as file:
                file.write(str(graph))
