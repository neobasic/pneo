import logging

import click
from nuke import gettext as _, Settings, fdocstr
from pneo.command.receiver.receiver_check import analyze_project

# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()

# ----------------------------------------------------------------------------
# CLICK: COMMAND CHECK
# ----------------------------------------------------------------------------

_check_short_help: str = _("Analyze the current project and report errors, but don't build target files.")


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
@click.pass_context
@fdocstr(_check_short_help)
def check(context: click.Context, keep_going: bool) -> None:
    logger.debug("Entering: keep_going=%s", keep_going)

    # proceed with the checking.
    analyze_project(keep_going)
