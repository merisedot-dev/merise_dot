import click
from click import Context
from rich.console import Console

# metadata
__version__ = "0.1.0"

# console reference
_CONSOLE = Console()


@click.group()
@click.version_option(__version__)
@click.pass_context
def main(ctx: Context, **kwargs) -> None:
    pass # nothing here, we just needed a functer


@click.command("mcd", help="Build the given MCD into a schematic")
def mk_mcd(**kwargs) -> None:
    pass
