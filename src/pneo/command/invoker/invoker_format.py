import logging
import os

import click
from nuke import gettext as _, Settings, fdocstr, p_error
from pneo.command.receiver.receiver_format import format_files

# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()

# ----------------------------------------------------------------------------
# CLICK: COMMAND FORMAT
# ----------------------------------------------------------------------------

_format_short_help: str = _("Format one or more NeoBASIC program files, or the source folder of the current project.")


@click.command(name="format", options_metavar=_("<OPTIONS>"), short_help=_format_short_help)
@click.option(
    "--keep-going",
    "-k",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Do not abort the format as soon as there is an error."),
)
@click.option(
    "--diff",
    "-d",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
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
@fdocstr(_format_short_help)
def formatter(context: click.Context, keep_going: bool, diff: bool, files: tuple) -> None:
    logger.debug("Entering: keep_going=%s, diff=%s, files=%s", keep_going, diff, files)

    # Check if each given file exists.
    for file_name in files:
        if not os.path.exists(file_name):
            p_error(_("Error: Source file '%s' does not exist."), file_name)

    # proceed with the formatting.
    format_files(files, keep_going, diff)
