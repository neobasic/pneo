import logging
from pathlib import Path

import click

from nuke import gettext as _, ngettext as _n, AppConfig, fdocstr, echo, p_trace, p_debug, p_info, p_warn, p_error, p_fatal


# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application settings.
app_config: AppConfig = AppConfig.get_instance()


# ----------------------------------------------------------------------------
# CLICK: COMMAND MAKE
# ----------------------------------------------------------------------------

_make_short_help: str = _("Compile the target directory and generate the binary executable.")


@click.command(options_metavar=_("<OPTIONS>"), short_help=_make_short_help)
@click.option(
    "--bin",
    "-b",
    required=False,
    type=click.Path(exists=False, dir_okay=True),
    default=Path("bin"),
    help=_("Specify where to place generated binary files."),
)
@click.option(
    "--nowarn",
    "-n",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Generate no warnings about the linking, only errors."),
)
@click.option(
    "--verbose",
    "-v",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Output messages about what the compiler is doing."),
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
def make(context: click.Context, bin: Path, nowarn: bool, verbose: bool, target: Path) -> None:
    logger.debug("Entering: bin=%s, nowarn=%s, verbose=%s, target=%s", bin, nowarn, verbose, target)

    pass
