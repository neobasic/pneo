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
# CLICK: COMMAND LOCK
# ----------------------------------------------------------------------------

lock_short_help: str = _("Create or update the current project's lockfile.")

@click.command(
    options_metavar=_("<OPTIONS>"),
    short_help=lock_short_help
)
@click.option(
    "--check", "-c",
    required=False,
    is_flag=True,
    default=False,
    type=click.BOOL,
    help=_("Check if the lockfile is up-to-date."),
)
@click.option(
    "--upgrade", "-u",
    required=False,
    is_flag=True,
    default=False,
    type=click.BOOL,
    help=_("Apply package upgrades, ignoring pinned versions in any existing output file."),
)
@click.pass_context
@fdocstr(lock_short_help)
def lock(context: click.Context, check: bool, upgrade: bool) -> None:
    # print(f"check: {check}, upgrade: {upgrade}")
    pass
