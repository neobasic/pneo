import logging
from pathlib import Path

import click

from nuke import gettext as _, ngettext as _n, Settings, fdocstr, echo, p_trace, p_debug, p_info, p_warn, p_error, p_fatal


# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()


# ----------------------------------------------------------------------------
# CLICK: COMMAND RUN
# ----------------------------------------------------------------------------

_run_short_help: str = _("Execute the binary executable in target directory or a local program.")


@click.command(options_metavar=_("<OPTIONS>"), short_help=_run_short_help)
@click.option(
    "--target",
    "-t",
    required=False,
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
    help=_("Target directory containing the binary executable."),
)
@click.option(
    "--script",
    "-s",
    required=False,
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
    help=_("Run the given source file as a NeoBASIC script."),
)
@click.option(
    "--offline",
    "-o",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Run without accessing the network (disable network access)."),
)
@click.pass_context
@fdocstr(_run_short_help)
def run(context: click.Context, target: Path, script: Path, offline: bool) -> None:
    logger.debug("Entering: target=%s, script=%s, offline=%s", target, script, offline)

    pass
