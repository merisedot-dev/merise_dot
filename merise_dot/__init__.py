import click
from click import Context

# inner command imports
from .commands import *

# metadata
__version__ = "1.3.0"


@click.group()
@click.version_option(__version__)
@click.pass_context
def main(_: Context) -> None:
    pass # nothing here, we just needed a functer


@main.command("mcd")
@click.pass_context
@click.argument("path")
@click.option(
    "-g", "--graph", help="Show the MCD graph in a PNG", is_flag=True)
@click.option(
    "-e", "--edit", help="Open editing options for the MCD", is_flag=True)
@click.option("-n", "--new", help="create a new MCD", is_flag=True)
def mcd(
        context: Context, path: str, graph: bool, edit: bool,
        new: bool) -> None:
    """Interact with and MCD graph.

    This graph needs to be stored at PATH, so the software can read it.
    The graph being stored needs to be MCD-compliant.

    Please see the options to check how one can interact with such graph.
    """
    mcd_cmd(context, path, graph, edit, new)


@main.command("mld")
@click.argument("path")
def mld(path: str) -> None:
    pass # TODO


@main.command("sql", help="Interact with SQL database definitions")
@click.argument("path")
def sql(path: str) -> None:
    pass # TODO
