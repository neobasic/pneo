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
# CLICK: COMMAND COMPILE
# ----------------------------------------------------------------------------

_compile_short_help: str = _("Parse and transpile one or more NeoBASIC program files.")


@click.command(options_metavar=_("<OPTIONS>"), short_help=_compile_short_help)
@click.option(
    "--target",
    "-t",
    required=False,
    type=click.Path(exists=False, dir_okay=True),
    default=Path("."),
    help=_("Specify where to place generated transpiled files."),
)
@click.option(
    "--nowarn",
    "-n",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Generate no warnings about the code, only errors."),
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
    "files",
    required=True,
    nargs=-1,
    type=click.STRING,
    metavar=_("<FILES>"),
)
@click.pass_context
@fdocstr(_compile_short_help)
def compile(
    context: click.Context, target: Path, nowarn: bool, verbose: bool, files: tuple
) -> None:
    logger.debug(
        "Entering: target={}, nowarn={}, verbose={}, files={}", target, nowarn, verbose, files
    )

    pass
