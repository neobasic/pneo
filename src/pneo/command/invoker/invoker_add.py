import logging
from pathlib import Path
from typing import Optional

import click

from nuke import gettext as _, ngettext as _n, AppConfig, fdocstr, echo, p_trace, p_debug, p_info, p_warn, p_error, p_fatal

from pneo.command.receiver.receiver_add import (
    LibraryLinking,
    add_dependency_path,
    add_dependency_web,
)


# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application settings.
app_config: AppConfig = AppConfig.get_instance()


# ----------------------------------------------------------------------------
# CLICK: COMMAND ADD
# ----------------------------------------------------------------------------

_add_short_help: str = _("Add one or more dependencies to the current project manifest file.")


@click.command(options_metavar=_("<OPTIONS>"), short_help=_add_short_help)
@click.option(
    "--path",
    "-p",
    required=False,
    type=click.Path(exists=True, file_okay=True, dir_okay=True),
    help=_("Filesystem path to local dependency to add."),
)
@click.option(
    "--static",
    "-s",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Library is copied directly into the final executable."),
)
@click.option(
    "--dynamic",
    "-d",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Library is separated from final executable and loaded at runtime."),
)
@click.argument(
    "packages",
    required=True,
    nargs=-1,
    type=click.STRING,
    metavar=_("<PACKAGES>"),
)
@click.pass_context
@fdocstr(_add_short_help)
def add(context: click.Context, path: Path, static: bool, dynamic: bool, packages: tuple) -> None:
    logger.debug(
        "Entering: path=%s, static=%s, dynamic=%s, packages=%s",
        path,
        static,
        dynamic,
        packages,
    )

    # dynamic is the default linking mode
    linking: LibraryLinking = LibraryLinking.DYNAMIC

    # can't use --static and --dynamic together.
    if static and dynamic:
        logger.error("Used both options '--static' and '--dinamic' in command ADD.")
        p_error(
            _(
                "Error: The flags <*'--static'*> and <*'--dinamic'*> are mutually exclusive; choose only one."
            )
        )
        exit(1)
    elif static:
        linking = LibraryLinking.STATIC

    # check where will get the dependency from:
    if path is None:
        add_dependency_web(packages, linking)
    else:
        dep_path: Path = Path(path)
        add_dependency_path(dep_path, packages, linking)
