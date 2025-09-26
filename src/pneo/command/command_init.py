import logging
from pathlib import Path

import click

import pneo


# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application settings.
app_config: pneo.AppConfig = pneo.getAppConfig()


# ----------------------------------------------------------------------------
# CLICK: COMMAND INIT
# ----------------------------------------------------------------------------

@click.command(options_metavar="<OPTIONS>")
@click.option(
    "--name",
    required=False,
    type=click.STRING,
    help="The name of the project",
)
@click.option(
    "--app",
    required=False,
    is_flag=True,
    default=False,
    type=click.BOOL,
    help="Create a project for an application",
)
@click.option(
    "--lib",
    required=False,
    is_flag=True,
    default=False,
    type=click.BOOL,
    help="Create a project for a library",
)
@click.argument(
    "path",
    required=True,
    default=Path("."),
    metavar="<PATH>",
    type=click.Path(exists=False, dir_okay=True, writable=True),
)
@click.pass_context
def init(context: click.Context, name: str, app: bool, lib: bool, path: Path) -> None:
    """
    Create a new NeoBASIC project in an existing <PATH> directory [default: .]
    """
    # print(f"name: {name}, app: {app}, lib: {lib}, path: {path}")
    pass
