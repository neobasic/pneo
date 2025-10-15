import logging

import click
from nuke import gettext as _, Settings, fdocstr
from pneo.command.receiver.receiver_lock import lock_project

# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()

# ----------------------------------------------------------------------------
# CLICK: COMMAND LOCK
# ----------------------------------------------------------------------------

_lock_short_help: str = _("Create or update the current project's lockfile.")


@click.command(options_metavar=_("<OPTIONS>"), short_help=_lock_short_help)
@click.option(
    "--check",
    "-c",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Check if the lockfile is up-to-date."),
)
@click.option(
    "--upgrade",
    "-u",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Apply package upgrades, ignoring pinned versions in any existing output file."),
)
@click.pass_context
@fdocstr(_lock_short_help)
def lock(context: click.Context, check: bool, upgrade: bool) -> None:
    logger.debug("Entering: check=%s, upgrade=%s", check, upgrade)

    # proceed with the locking.
    lock_project(check, upgrade)
