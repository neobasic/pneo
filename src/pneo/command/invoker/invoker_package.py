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
# CLICK: COMMAND PACKAGE
# ----------------------------------------------------------------------------

package_short_help: str = _("Assemble the compiled binaries into a distributable package.")

@click.command(
    options_metavar=_("<OPTIONS>"),
    short_help=package_short_help
)
@click.option(
    "--dist", "-d",
    required=False,
    type=click.Path(exists=False, dir_okay=True),
    default=Path('dist'),
    help=_("Specify where to place generated package files."),
)
@click.option(
    "--nowarn", "-n",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Generate no warnings about the packaging, only errors."),
)
@click.option(
    "--verbose", "-v",
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
    default=Path('bin'),
    metavar=_("<BIN>")
)
@click.pass_context
@fdocstr(package_short_help)
def package(context: click.Context, dist: Path, nowarn: bool, verbose: bool, bin: Path) -> None:
    # print(f"dist: {dist}, nowarn: {nowarn}, verbose: {verbose}, bin: {bin}")
    pass
