import pzp
from click import Context

from merise_dot.dot import MCDBuilder
from merise_dot.model import Graph, graph_parse
from .edit import MCDEditCmd


# actual command code
def mcd_cmd(ctx: Context, path: str, g: bool, e: bool, n: bool) -> None:
    print(f"Opening MCD in {path}")
    graph: Graph = None

    # Graph parsing
    if not n:
        contents: str = ""
        with open(path, 'r') as file:
            contents = file.reads()
        graph = graph_parse(contents)
    else: # the "new" flag was passed
        print("Enter MCD name : ", end="")
        name: str = input()
        if not name:
            exit(-1) # Why the fluff did you not input something
        graph = Graph(name)

    # smol hack for mainloop
    if n: # new flag was passed
        choice: bool = pzp.confirm(
            "Do you wish editing the MCD graph ?", default=False)
        if not choice:
            exit(0)
        e = True # flag manipulation for later
        with open(path, 'w') as file:
            file.write(str(graph))

    if e: # edition mainloop
        MCDEditCmd().edit(graph, path)

    if g: # rendering flag switched on
        grbld = MCDBuilder(graph)
        grbld.build(f"{name}.png")
        print(f"MCD {name} rendered")
