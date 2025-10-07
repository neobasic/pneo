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
    type=click.BOOL,
    default=False,
    help=_("Display what would be deleted without deleting anything."),
)
@click.option(
    "--quiet", "-q",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Specifies quiet mode, not prompting for delete confirmation."),
)
@click.argument(
    "path",
    required=True,
    type=click.Path(exists=True, dir_okay=True, writable=True),
    default=Path("."),
    metavar=_("<PATH>"),
)
@click.pass_context
@fdocstr(clean_short_help)
def clean(context: click.Context, keep: bool, quiet: bool, path: Path) -> None:
    # print(f"keep: {keep}, quiet: {quiet}, path: {path}")
    pass
