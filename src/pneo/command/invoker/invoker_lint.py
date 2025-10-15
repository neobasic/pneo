import logging
from pathlib import Path

import click
from nuke import gettext as _, Settings, fdocstr
from pneo.command.receiver.receiver_lint import lint_file

# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()

# ----------------------------------------------------------------------------
# CLICK: COMMAND LINT
# ----------------------------------------------------------------------------

_lint_short_help: str = _(
    "Run full semantic analysis on a single NeoBASIC program file, primarily for testing and debugging outside of a running editor.")


@click.command(options_metavar=_("<OPTIONS>"), short_help=_lint_short_help)
@click.option(
    "--keep-going",
    "-k",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Do not abort the analysis as soon as there is an error."),
)
@click.argument(
    "file",
    required=True,
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
    metavar=_("<FILE>"),
)
@click.pass_context
@fdocstr(_lint_short_help)
def lint(context: click.Context, keep_going: bool, file: Path) -> None:
    logger.debug("Entering: keep_going=%s, file=%s", keep_going, file)

    # proceed with the linting.
    lint_file(file, keep_going)
