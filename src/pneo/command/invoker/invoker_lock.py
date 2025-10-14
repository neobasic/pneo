import logging
from pathlib import Path

import click

from nuke import gettext as _, ngettext as _n, AppConfig, fdocstr, echo, p_trace, p_debug, p_info, p_warn, p_error, p_fatal


# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application settings.
app_config: AppConfig = AppConfig.get_instance()


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

    pass
