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
# CLICK: COMMAND LINT
# ----------------------------------------------------------------------------

lint_short_help: str = _("Run full semantic analysis on a single NeoBASIC program file, primarily for testing and debugging outside of a running editor.")

@click.command(
    options_metavar=_("<OPTIONS>"), 
    short_help=lint_short_help
)
@click.option(
    "--keep-going", "-k",
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
@fdocstr(lint_short_help)
def lint(context: click.Context, keep_going: bool, file: Path) -> None:
    # print(f"keep_going: {keep_going}, file: {file}")
    pass
