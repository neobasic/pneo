import logging
from pathlib import Path
from builtins import _, fdocstr

import pneo

import click


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

init_short_help: str = _("Create a new NeoBASIC project in an existing <PATH> directory. [default: .]")

@click.command(
    options_metavar=_("<OPTIONS>"),
    short_help=init_short_help
)
@click.option(
    "--name", "-n",
    required=False,
    type=click.STRING,
    help=_("The name of the project."),
)
@click.option(
    "--app", "-a",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Create a project for an application."),
)
@click.option(
    "--lib", "-l",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Create a project for a library."),
)
@click.argument(
    "path",
    required=True,
    type=click.Path(exists=False, dir_okay=True, writable=True),
    default=Path("."),
    metavar=_("<PATH>"),
)
@click.pass_context
@fdocstr(init_short_help)
def init(context: click.Context, name: str, app: bool, lib: bool, path: Path) -> None:
    # print(f"name: {name}, app: {app}, lib: {lib}, path: {path}")
    pass
