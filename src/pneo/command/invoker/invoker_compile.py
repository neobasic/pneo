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
# CLICK: COMMAND COMPILE
# ----------------------------------------------------------------------------

compile_short_help: str = _("Parse and transpile one or more NeoBASIC program files.")

@click.command(
    options_metavar=_("<OPTIONS>"),
    short_help=compile_short_help
)
@click.option(
    "--target", "-t",
    required=False,
    type=click.Path(exists=False, dir_okay=True),
    default=Path('.'),
    help=_("Specify where to place generated transpiled files."),
)
@click.option(
    "--nowarn", "-n",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Generate no warnings about the code, only errors."),
)
@click.option(
    "--verbose", "-v",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Output messages about what the compiler is doing."),
)
@click.argument(
    "files",
    required=True,
    nargs=-1,
    type=click.STRING,
    metavar=_("<FILES>"),
)
@click.pass_context
@fdocstr(compile_short_help)
def compile(context: click.Context, target: Path, nowarn: bool, verbose: bool, files: tuple) -> None:
    # print(f"target: {target}, nowarn: {nowarn}, verbose: {verbose}, files: {files}")
    pass
