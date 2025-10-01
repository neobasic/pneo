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
# CLICK: COMMAND CLEAN
# ----------------------------------------------------------------------------

clean_short_help: str = _("Remove artifacts of project that pneo has generated in the past, in an existing <PATH> directory. [default: .]")

@click.command(
    options_metavar=_("<OPTIONS>"),
    short_help=clean_short_help
)
@click.option(
    "--keep", "-k",
    required=False,
    is_flag=True,
    default=False,
    type=click.BOOL,
    help=_("Display what would be deleted without deleting anything."),
)
@click.option(
    "--quiet", "-q",
    required=False,
    is_flag=True,
    default=False,
    type=click.BOOL,
    help=_("Specifies quiet mode, not prompting for delete confirmation."),
)
@click.argument(
    "path",
    required=True,
    default=Path("."),
    metavar=_("<PATH>"),
    type=click.Path(exists=True, dir_okay=True, writable=True),
)
@click.pass_context
@fdocstr(clean_short_help)
def clean(context: click.Context, keep: bool, quiet: bool, path: Path) -> None:
    # print(f"keep: {keep}, quiet: {quiet}, path: {path}")
    pass
