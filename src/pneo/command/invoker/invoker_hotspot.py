import logging
from pathlib import Path

import click
from nuke import gettext as _, Settings, fdocstr, p_error
from nuke.utils.shell import make_accessible_dir, check_readable_dir
from pneo.command.receiver.receiver_hotspot import start_hotspot

# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()

# ----------------------------------------------------------------------------
# CLICK: COMMAND HOTSPOT
# ----------------------------------------------------------------------------

_hotspot_short_help: str = _("Stat the hotspot server for incremental compilation in real time, as code is edited.")


@click.command(options_metavar=_("<OPTIONS>"), short_help=_hotspot_short_help)
@click.option(
    "--target",
    "-t",
    required=False,
    type=click.Path(exists=False, dir_okay=True),
    default=Path("target"),
    help=_("Target directory for all generated artifacts. [default: target]"),
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
    "src",
    required=False,
    type=click.Path(exists=True, dir_okay=True),
    default=Path("src"),
    metavar=_("<SRC>"),
)
@click.pass_context
@fdocstr(_hotspot_short_help)
def hotspot(context: click.Context, target: Path, no_warn: bool, src: Path) -> None:
    logger.debug("Entering: target=%s, no_warn=%s, src=%s", target, no_warn, src)

    # if user indicated a target dir, check if it is accessible.
    if target and not make_accessible_dir(target):
        p_error(_("Error: Target directory '%s' cannot be accessed or you don't have permission to write to it."),
                target)
        exit(1)

    # if user indicated a source dir, check if it exists and is readable.
    if src and not check_readable_dir(src):
        p_error(_("Error: Source directory '%s' does not exist or can't be read."), src)
        exit(1)

    # proceed with starting the hotspot server.
    start_hotspot(src, target, no_warn)
