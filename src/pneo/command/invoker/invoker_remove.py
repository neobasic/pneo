import logging
from pathlib import Path
from builtins import _, fdocstr

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
# CLICK: COMMAND REMOVE
# ----------------------------------------------------------------------------

remove_short_help: str = _("Remove dependencies from the current project manifest file.")

@click.command(
    options_metavar=_("<OPTIONS>"),
    short_help=remove_short_help
)
@click.option(
    "--locked", "-l",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Remove dependencies without re-locking the project."),
)
@click.option(
    "--check", "-c",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Check whether removing the package will cause issues in the project."),
)
@click.argument(
    "packages",
    required=True,
    nargs=-1,
    type=click.STRING,
    metavar=_("<PACKAGES>"),
)
@click.pass_context
@fdocstr(remove_short_help)
def remove(context: click.Context, check: bool, locked: bool, packages: tuple) -> None:
    # print(f"check: {check}, locked: {locked}, packages: {packages}")
    pass
