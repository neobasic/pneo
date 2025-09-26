import logging
from pathlib import Path

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
# CLICK: COMMAND CLEAN
# ----------------------------------------------------------------------------

@click.command(options_metavar="<OPTIONS>")
@click.option(
    "--keep",
    required=False,
    is_flag=True,
    default=False,
    type=click.BOOL,
    help="Display what would be deleted without deleting anything",
)
@click.option(
    "--quiet",
    required=False,
    is_flag=True,
    default=False,
    type=click.BOOL,
    help="Specifies quiet mode, not prompting for delete confirmation",
)
@click.argument(
    "path",
    required=True,
    default=Path("."),
    metavar="<PATH>",
    type=click.Path(exists=True, dir_okay=True, writable=True),
)
@click.pass_context
def clean(context: click.Context, keep: bool, quiet: bool, path: Path) -> None:
    """
    Remove artifacts of project that pneo has generated in the past, in an existing <PATH> directory [default: .]
    """
    # print(f"keep: {keep}, quiet: {quiet}, path: {path}")
    pass
