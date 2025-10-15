import logging
from pathlib import Path

import click
from nuke import gettext as _, Settings, fdocstr

# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()

# ----------------------------------------------------------------------------
# CLICK: COMMAND VENV
# ----------------------------------------------------------------------------

_venv_short_help: str = _(
    "Create a virtual environment named <PATH> in the working directory; defaults to `.venv` if not provided.")


@click.command(options_metavar=_("<OPTIONS>"), short_help=_venv_short_help)
@click.option(
    "--check",
    "-c",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Just check if all dependencies are installed and up-to-date, don't do anything."),
)
@click.option(
    "--sync",
    "-s",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Ensures all dependencies are installed and up-to-date with the lockfile."),
)
@click.option(
    "--locked",
    "-l",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Assert that the lockfile will remain unchanged."),
)
@click.argument(
    "path", required=False, type=click.Path(exists=False, dir_okay=True), metavar=_("<PATH>")
)
@click.pass_context
@fdocstr(_venv_short_help)
def venv(context: click.Context, check: bool, sync: bool, locked: bool, path: Path) -> None:
    logger.debug("Entering: check=%s, sync=%s, locked=%s, path=%s", check, sync, locked, path)

    pass
