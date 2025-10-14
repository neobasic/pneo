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
# CLICK: COMMAND BUILD
# ----------------------------------------------------------------------------

_build_short_help: str = _("Compile the current project and build the target directory.")


@click.command(options_metavar=_("<OPTIONS>"), short_help=_build_short_help)
@click.option(
    "--target",
    "-t",
    required=False,
    type=click.Path(exists=False, dir_okay=True),
    default=Path("target"),
    help=_("Target directory for all generated artifacts."),
)
@click.option(
    "--keep-going",
    "-k",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Do not abort the build as soon as there is an error."),
)
@click.option(
    "--verbose",
    "-v",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Use verbose output on console."),
)
@click.argument(
    "src",
    required=False,
    type=click.Path(exists=True, dir_okay=True),
    default=Path("src"),
    metavar=_("<SRC>"),
)
@click.pass_context
@fdocstr(_build_short_help)
def build(context: click.Context, target: Path, keep_going: bool, verbose: bool, src: Path) -> None:
    logger.debug(
        "Entering: target=%s, keep_going=%s, verbose=%s, src=%s", target, keep_going, verbose, src
    )

    pass
