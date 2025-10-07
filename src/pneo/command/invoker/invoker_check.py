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
# CLICK: COMMAND CHECK
# ----------------------------------------------------------------------------

check_short_help: str = _("Analyze the current project and report errors, but don't build target files.")

@click.command(
    options_metavar=_("<OPTIONS>"), 
    short_help=check_short_help
)
@click.option(
    "--keep-going", "-k",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Do not abort the check as soon as there is an error."),
)              
@click.option(
    "--verbose", "-v",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Use verbose output on console."),
)
@click.pass_context
@fdocstr(check_short_help)
def check(context: click.Context, keep_going: bool, verbose: bool) -> None:
    # print(f"keep_going: {keep_going}, verbose: {verbose}")
    pass
