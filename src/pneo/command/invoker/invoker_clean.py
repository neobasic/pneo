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
# CLICK: COMMAND CLEAN
# ----------------------------------------------------------------------------

_clean_short_help: str = _(
    "Remove artifacts of project that pneo has generated in the past, in an existing <PATH> directory. [default: .]"
)


@click.command(options_metavar=_("<OPTIONS>"), short_help=_clean_short_help)
@click.option(
    "--keep",
    "-k",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Display what would be deleted without deleting anything."),
)
@click.option(
    "--quiet",
    "-q",
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
@fdocstr(_clean_short_help)
def clean(context: click.Context, keep: bool, quiet: bool, path: Path) -> None:
    logger.debug("Entering: keep=%s, quiet=%s, path=%s", keep, quiet, path)

    pass
