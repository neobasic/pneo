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
# CLICK: COMMAND FORMAT
# ----------------------------------------------------------------------------

format_short_help: str = _("Format one or more NeoBASIC program files, or the source folder of the current project.")

@click.command(
    options_metavar=_("<OPTIONS>"),
    short_help=format_short_help
)
@click.option(
    "--keep-going", "-k",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Do not abort the format as soon as there is an error."),
)
@click.option(
    "--diff", "-d",
    required=False,
    is_flag=True,
    default=False,
    type=click.BOOL,
    help=_("Show a diff of formatting changes without applying them."),
)
@click.argument(
    "files",
    required=False,
    nargs=-1,
    type=click.STRING,
    metavar=_("<FILES>"),
)
@click.pass_context
@fdocstr(format_short_help)
def format(context: click.Context, keep_going: bool, diff: bool, files: tuple) -> None:
    # print(f"keep_going: {keep_going}, diff: {diff}, files: {files}")
    pass
