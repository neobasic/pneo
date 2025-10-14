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
# CLICK: COMMAND PACKAGE
# ----------------------------------------------------------------------------

_package_short_help: str = _("Assemble the compiled binaries into a distributable package.")


@click.command(options_metavar=_("<OPTIONS>"), short_help=_package_short_help)
@click.option(
    "--dist",
    "-d",
    required=False,
    type=click.Path(exists=False, dir_okay=True),
    default=Path("dist"),
    help=_("Specify where to place generated package files."),
)
@click.option(
    "--nowarn",
    "-n",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Generate no warnings about the packaging, only errors."),
)
@click.option(
    "--verbose",
    "-v",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Output messages about what the assembler is doing."),
)
@click.argument(
    "bin",
    required=False,
    type=click.Path(exists=True, dir_okay=True),
    default=Path("bin"),
    metavar=_("<BIN>"),
)
@click.pass_context
@fdocstr(_package_short_help)
def package(context: click.Context, dist: Path, nowarn: bool, verbose: bool, bin: Path) -> None:
    logger.debug("Entering: dist=%s, nowarn=%s, verbose=%s, bin=%s", dist, nowarn, verbose, bin)

    pass
