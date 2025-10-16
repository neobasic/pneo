import logging
from pathlib import Path

import click
from nuke import gettext as _, Settings, fdocstr
from nuke.formatters.print_color import p_error
from nuke.utils.shell import make_accessible_dir, check_readable_dir
from pneo.command.receiver.receiver_package import package_binary

# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()

# ----------------------------------------------------------------------------
# CLICK: COMMAND PACKAGE
# ----------------------------------------------------------------------------

_package_short_help: str = _("Assemble the compiled binaries into a distributable package.")


@click.command(options_metavar=_("<OPTIONS>"), short_help=_package_short_help)
@click.option(
    "--dist-dir",
    "-d",
    required=False,
    type=click.Path(exists=False, dir_okay=True),
    default=Path("dist"),
    help=_("Specify where to place generated package files."),
)
@click.option(
    "--no-warn",
    "-n",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Generate no warnings about the packaging, only errors."),
)
@click.argument(
    "bin-dir",
    required=False,
    type=click.Path(exists=True, dir_okay=True),
    default=Path("bin"),
    metavar=_("<BIN-DIR>"),
)
@click.pass_context
@fdocstr(_package_short_help)
def package(context: click.Context, dist_dir: Path, no_warn: bool, bin_dir: Path) -> None:
    logger.debug("Entering: dist_dir=%s, no_warn=%s, bin_dir=%s", dist_dir, no_warn, bin_dir)

    # if user indicated a dist dir, check if it is accessible.
    if dist_dir and not make_accessible_dir(dist_dir):
        p_error(_("Error: Distribution directory '%s' cannot be accessed or you don't have permission to write to it."),
                dist_dir)
        exit(1)

    # if user indicated a binary dir, check if it exists and is readable.
    if bin_dir and not check_readable_dir(bin_dir):
        p_error(_("Error: Target directory '%s' does not exist or can't be read."), bin_dir)
        exit(1)

    # proceed with the packaging.
    package_binary(dist_dir, bin_dir, no_warn)
