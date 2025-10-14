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
# CLICK: COMMAND LIST
# ----------------------------------------------------------------------------

_list_short_help: str = _("List all NeoBASIC modules and translation units in current project.")


@click.command(options_metavar=_("<OPTIONS>"), short_help=_list_short_help)
@click.option(
    "--module",
    "-m",
    required=False,
    type=click.STRING,
    help=_("Only list submodules and source files of a given module."),
)
@click.option(
    "--absolute-path",
    "-a",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Display source files with their absolute path."),
)
@click.option(
    "--only-modules",
    "-o",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("List only modules and submodules."),
)
@click.option(
    "--long-table",
    "-l",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Display extended source file metadata, as a table."),
)
@click.pass_context
@fdocstr(_list_short_help)
def list(
    context: click.Context, module: str, absolute_path: bool, only_modules: bool, long_table: bool
) -> None:
    logger.debug(
        "Entering: module=%s, absolute_path=%s, only_modules=%s, long_table=%s",
        module,
        absolute_path,
        only_modules,
        long_table,
    )

    pass
