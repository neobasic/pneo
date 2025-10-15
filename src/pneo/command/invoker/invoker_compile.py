import logging
import os
from pathlib import Path

import click
from nuke import gettext as _, Settings, fdocstr
from nuke.formatters.print_color import p_error
from nuke.utils.shell import make_accessible_dir
from pneo.command.receiver.receiver_compile import compile_files

# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()

# ----------------------------------------------------------------------------
# CLICK: COMMAND COMPILE
# ----------------------------------------------------------------------------

_compile_short_help: str = _("Parse and transpile one or more NeoBASIC program files.")


@click.command(name="compile", options_metavar=_("<OPTIONS>"), short_help=_compile_short_help)
@click.option(
    "--target",
    "-t",
    required=False,
    type=click.Path(exists=False, dir_okay=True),
    default=Path("."),
    help=_("Specify where to place generated transpiled files. [Default: .]"),
)
@click.option(
    "--no-warn",
    "-n",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Generate no warnings about the code, only errors."),
)
@click.argument(
    "files",
    required=True,
    nargs=-1,
    type=click.STRING,
    metavar=_("<FILES>"),
)
@click.pass_context
@fdocstr(_compile_short_help)
def compiler(context: click.Context, target: Path, no_warn: bool, files: tuple) -> None:
    logger.debug("Entering: target=%s, no_warn=%s, files=%s", target, no_warn, files)

    # if user indicated a target dir, check if it is accessible.
    if target and not make_accessible_dir(target):
        p_error(_("Error: Target directory '%s' cannot be accessed or you don't have permission to written to it."),
                target)
        exit(1)

    # Check if each given file exists.
    for file_name in files:
        if not os.path.exists(file_name):
            p_error(_("Error: Source file '%s' does not exist."), file_name)

    # proceed with the compiling.
    compile_files(target, files, no_warn)
