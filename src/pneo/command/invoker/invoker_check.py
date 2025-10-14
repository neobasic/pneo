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
# CLICK: COMMAND CHECK
# ----------------------------------------------------------------------------

_check_short_help: str = _(
    "Analyze the current project and report errors, but don't build target files."
)


@click.command(options_metavar=_("<OPTIONS>"), short_help=_check_short_help)
@click.option(
    "--keep-going",
    "-k",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Do not abort the check as soon as there is an error."),
)
@click.option(
    "--verbose",
    "-v",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Use verbose output on console."),
)
@click.pass_context
@fdocstr(_check_short_help)
def check(context: click.Context, keep_going: bool, verbose: bool) -> None:
    logger.debug("Entering: keep_going=%s, verbose=%s", keep_going, verbose)

    pass
