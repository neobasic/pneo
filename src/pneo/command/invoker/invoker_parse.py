import logging
import os
from pathlib import Path

import click
from nuke import gettext as _, Settings, fdocstr
from nuke.formatters.print_color import p_error
from pneo.command.receiver.receiver_parse import parse_file

# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()

# ----------------------------------------------------------------------------
# CLICK: COMMAND PARSE
# ----------------------------------------------------------------------------

_parse_short_help: str = _(
    "Parse a single NeoBASIC program file and output the abstract syntax tree (AST) or other structured data. This can be used for debugging the parser logic.")


@click.command(options_metavar=_("<OPTIONS>"), short_help=_parse_short_help)
@click.option(
    "--depth",
    "-d",
    required=False,
    type=click.IntRange(1, 255, clamp=True),
    default=100,
    help=_("Maximum display depth of the abstract syntax tree (AST). [default: 100]"),
)
@click.option(
    "--all-info",
    "-a",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Show detailed information of all symbols in the abstract syntax tree (AST)."),
)
@click.option(
    "--short",
    "-s",
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
@fdocstr(_parse_short_help)
def parse(context: click.Context, depth: int, all_info: bool, short: bool, file: Path) -> None:
    logger.debug("Entering: depth=%s, all_info=%s, short=%s, file=%s", depth, all_info, short, file)

    # Check if the given file exists.
    if not os.path.exists(file):
        p_error(_("Error: Source file '%s' does not exist."), file)

    # proceed with the parsing.
    parse_file(file, depth, all_info, short)
