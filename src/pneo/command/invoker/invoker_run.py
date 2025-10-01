import logging
from pathlib import Path
from builtins import _, fdocstr

import click

import pneo


# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application settings.
app_config: pneo.AppConfig = pneo.getAppConfig()


# ----------------------------------------------------------------------------
# CLICK: COMMAND RUN
# ----------------------------------------------------------------------------

run_short_help: str = _("Execute the binary executable in target directory or a local program.")

@click.command(
    options_metavar=_("<OPTIONS>"),
    short_help=run_short_help
)
@click.option(
    "--target", "-t",
    required=False,
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
    help=_("Target directory containing the binary executable."),
)
@click.option(
    "--script", "-s",
    required=False,
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
    help=_("Run the given source file as a NeoBASIC script."),
)
@click.option(
    "--offline", "-o",
    required=False,
    is_flag=True,
    default=False,
    type=click.BOOL,
    help=_("Run without accessing the network (disable network access)."),
)                                    
@click.pass_context
@fdocstr(run_short_help)
def run(context: click.Context, target: Path, script: Path, offline: bool) -> None:
    # print(f"target: {target}, script: {script}, offline: {offline}")
    pass
