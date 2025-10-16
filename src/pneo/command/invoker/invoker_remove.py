import logging

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
# CLICK: COMMAND REMOVE
# ----------------------------------------------------------------------------

_remove_short_help: str = _("Remove dependencies from the current project manifest file.")


@click.command(options_metavar=_("<OPTIONS>"), short_help=_remove_short_help)
@click.option(
    "--locked",
    "-l",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Remove dependencies without re-locking the project."),
)
@click.option(
    "--check",
    "-c",
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
@fdocstr(_remove_short_help)
def remove(context: click.Context, check: bool, locked: bool, packages: tuple) -> None:
    logger.debug("Entering: check=%s, locked=%s, packages=%s", check, locked, packages)

    # proceed with the dependency removing.
