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
# CLICK: COMMAND BUILD
# ----------------------------------------------------------------------------

build_short_help: str = _("Compile the current project and build the target directory.")

@click.command(
    options_metavar=_("<OPTIONS>"),
    short_help=build_short_help
)
@click.option(
    "--target", "-t",
    required=False,
    type=click.Path(exists=False, dir_okay=True),
    default=Path('target'),
    help=_("Target directory for all generated artifacts."),
)
@click.option(
    "--keep-going", "-k",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Do not abort the build as soon as there is an error."),
)              
@click.option(
    "--verbose", "-v",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Use verbose output on console."),
)
@click.argument(
    "src",
    required=False,
    default=Path('src'),
    type=click.Path(exists=True, dir_okay=True),
    metavar=_("<SRC>")
)
@click.pass_context
@fdocstr(build_short_help)
def build(context: click.Context, target: Path, keep_going: bool, verbose: bool, src: Path) -> None:
    # print(f"target: {target}, keep_going: {keep_going}, verbose: {verbose}, src: {src}")
    pass
