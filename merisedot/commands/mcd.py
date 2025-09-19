from click import Context
from rich.console import Console


# actual command code
def mcd_cmd(
        console: Console, ctx: Context, path: str, g: bool, e: bool,
        n: bool) -> None:
    console.print(f"Opening MCD in {path}")
    # TODO check MCD compliancy
