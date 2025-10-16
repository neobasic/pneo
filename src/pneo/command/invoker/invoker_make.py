import logging
from pathlib import Path

import click
from nuke import gettext as _, Settings, fdocstr
from nuke.formatters.print_color import p_error
from nuke.utils.shell import make_accessible_dir, check_readable_dir
from pneo.command.receiver.receiver_make import make_binary

# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()

# ----------------------------------------------------------------------------
# CLICK: COMMAND MAKE
# ----------------------------------------------------------------------------

_make_short_help: str = _("Compile the target directory and generate the binary executable.")


@click.command(options_metavar=_("<OPTIONS>"), short_help=_make_short_help)
@click.option(
    "--bin-dir",
    "-b",
    required=False,
    type=click.Path(exists=False, dir_okay=True),
    default=Path("bin"),
    help=_("Specify where to place generated binary files."),
)
@click.option(
    "--no-warn",
    "-n",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Generate no warnings about the linking, only errors."),
)
@click.argument(
    "target",
    required=False,
    type=click.Path(exists=True, dir_okay=True),
    default=Path("target"),
    metavar=_("<TARGET>"),
)
@click.pass_context
@fdocstr(_make_short_help)
def make(context: click.Context, bin_dir: Path, no_warn: bool, target: Path) -> None:
    logger.debug("Entering: bin_dir=%s, no_warn=%s, target=%s", bin_dir, no_warn, target)

    # if user indicated a bin dir, check if it is accessible.
    if bin_dir and not make_accessible_dir(bin_dir):
        p_error(_("Error: Binary directory '%s' cannot be accessed or you don't have permission to write to it."),
                bin_dir)
        exit(1)

    # if user indicated a target dir, check if it exists and is readable.
    if target and not check_readable_dir(target):
        p_error(_("Error: Target directory '%s' does not exist or can't be read."), target)
        exit(1)

    # proceed with the making.
    make_binary(target, bin_dir, no_warn)
