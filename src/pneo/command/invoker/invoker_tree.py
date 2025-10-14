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
# CLICK: COMMAND TREE
# ----------------------------------------------------------------------------

_tree_short_help: str = _(
    "Display the dependency tree of current project, or some other project manifest file."
)


@click.command(options_metavar=_("<OPTIONS>"), short_help=_tree_short_help)
@click.option(
    "--path",
    "-p",
    required=False,
    type=click.Path(exists=True, file_okay=True, dir_okay=True),
    help=_("Path to the project manifest file."),
)
@click.option(
    "--depth",
    "-d",
    required=False,
    type=click.IntRange(1, 255, clamp=True),
    default=255,
    help=_("Maximum display depth of the dependency tree. [default: 255]"),
)
@click.option(
    "--outdated",
    "-o",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Show the latest available version of each package in the tree."),
)
@click.option(
    "--show-sizes",
    "-s",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Show sizes of all packages in the tree."),
)
@click.pass_context
@fdocstr(_tree_short_help)
def tree(context: click.Context, path: Path, depth: int, outdated: bool, show_sizes: bool) -> None:
    logger.debug(
        "Entering: path=%s, depth=%s, outdated=%s, show_sizes=%s", path, depth, outdated, show_sizes
    )

    pass
