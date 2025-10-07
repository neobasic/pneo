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
# CLICK: COMMAND ADD
# ----------------------------------------------------------------------------

add_short_help: str = _("Add one or more dependencies to the current project manifest file.")

@click.command(
    options_metavar=_("<OPTIONS>"),
    short_help=add_short_help
)
@click.option(
    "--path", "-p",
    required=False,
    type=click.Path(exists=True, file_okay=True, dir_okay=True),
    help=_("Filesystem path to local dependency to add."),
)
@click.option(
    "--static", "-s",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Library is copied directly into the final executable."),
)
@click.option(
    "--dynamic", "-d",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Library is separated from final executable and loaded at runtime."),
)
@click.argument(
    "packages",
    required=True,
    nargs=-1,
    type=click.STRING,
    metavar=_("<PACKAGES>"),
)
@click.pass_context
@fdocstr(add_short_help)
def add(context: click.Context, path: Path, static: bool, dynamic: bool, packages: tuple) -> None:
    # print(f"path: {path}, static: {static}, dynamic: {dynamic}, packages: {packages}")
    pass
