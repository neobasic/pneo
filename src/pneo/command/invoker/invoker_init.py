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
# CLICK: COMMAND INIT
# ----------------------------------------------------------------------------

_init_short_help: str = _(
    "Create a new NeoBASIC project in an existing <PATH> directory. [default: .]"
)


@click.command(options_metavar=_("<OPTIONS>"), short_help=_init_short_help)
@click.option(
    "--name",
    "-n",
    required=False,
    type=click.STRING,
    help=_("The name of the project."),
)
@click.option(
    "--app",
    "-a",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Create a project for an application."),
)
@click.option(
    "--lib",
    "-l",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Create a project for a library."),
)
@click.argument(
    "path",
    required=True,
    type=click.Path(exists=False, dir_okay=True, writable=True),
    default=Path("."),
    metavar=_("<PATH>"),
)
@click.pass_context
@fdocstr(_init_short_help)
def init(context: click.Context, name: str, app: bool, lib: bool, path: Path) -> None:
    logger.debug("Entering: name=%s, app=%s, lib=%s, path=%s", name, app, lib, path)

    pass
