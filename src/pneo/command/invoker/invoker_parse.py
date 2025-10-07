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
# CLICK: COMMAND PARSE
# ----------------------------------------------------------------------------

parse_short_help: str = _("Parse a single NeoBASIC program file and output the abstract syntax tree (AST) or other structured data. This can be used for debugging the parser logic.")

@click.command(
    options_metavar=_("<OPTIONS>"),
    short_help=parse_short_help
)
@click.option(
    "--depth", "-d",
    required=False,
    type=click.IntRange(1, 255, clamp=True),
    default=100,
    help=_("Maximum display depth of the abstract syntax tree (AST). [default: 100]"),
)
@click.option(
    "--all", "-a",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Show detailed information of all symbols in the abstract syntax tree (AST)."),
)
@click.option(
    "--short", "-s",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Only print main symbols in the abstract syntax tree (AST)."),
)
@click.argument(
    "file",
    required=True,
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
    metavar=_("<FILE>"),
)
@click.pass_context
@fdocstr(parse_short_help)
def parse(context: click.Context, depth: int, all: bool, short: bool, file: Path) -> None:
    # print(f"depth: {depth}, all: {all}, short: {short}, file: {file}")
    pass
