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
# CLICK: COMMAND LIST
# ----------------------------------------------------------------------------

list_short_help: str = _("List all NeoBASIC modules and translation units in current project.")

@click.command(
    options_metavar=_("<OPTIONS>"),
    short_help=list_short_help
)
@click.option(
    "--module", "-m",
    required=False,
    type=click.STRING,
    help=_("Only list submodules and source files of a given module."),
)
@click.option(
    "--absolute-path", "-a",
    required=False,
    is_flag=True,
    default=False,
    type=click.BOOL,
    help=_("Display source files with their absolute path."),
)
@click.option(
    "--only-modules", "-o",
    required=False,
    is_flag=True,
    default=False,
    type=click.BOOL,
    help=_("List only modules and submodules."),
)
@click.option(
    "--long-table", "-l",
    required=False,
    is_flag=True,
    default=False,
    type=click.BOOL,
    help=_("Display extended source file metadata, as a table."),
)
@click.pass_context
@fdocstr(list_short_help)
def list(context: click.Context, module: str, absolute_path: bool, only_modules: bool, long_table: bool) -> None:
    # print(f"module: {module}, absolute_path: {absolute_path}, only_modules: {only_modules}, long_table: {long_table}")
    pass
