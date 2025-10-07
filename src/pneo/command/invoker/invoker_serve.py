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
# CLICK: COMMAND SERVE
# ----------------------------------------------------------------------------

serve_short_help: str = _("Run in language server mode, ready to handle requests from a client (the editor).")

@click.command(
    options_metavar=_("<OPTIONS>"),
    short_help=serve_short_help
)
@click.option(
    "--stdio", "-s",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Instructs the server to communicate over its standard input (stdin) and standard output (stdout)."),
)
@click.option(
    "--socket-port", "-p",
    required=False,
    type=click.IntRange(0, 65535, clamp=True),
    help=_("Instructs the server to listen on a specific TCP port for a client connection (socket). Used for remote development, servers running as persistent services, or clients that prefer TCP, often enabling multiple clients to connect to a single server instance."),
)
@click.option(
    "--limit-results", "-l",
    required=False,
    type=click.IntRange(1, 100, clamp=True),
    default=10,
    help=_("Limit completion items. [default: 10]"),
)
@click.option(
    "--verbose", "-v",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Increases the server's logging and output verbosity."),
)
@click.option(
    "--quiet", "-q",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Decreases the server's logging and output verbosity (opposite of verbose)."),
)
@click.pass_context
@fdocstr(serve_short_help)
def serve(context: click.Context, stdio: bool, socket_port: int, limit_results: int, verbose: bool, quiet: bool) -> None:
    # print(f"stdio: {stdio}, socket_port: {socket_port}, limit_results: {limit_results}, verbose: {verbose}, quiet: {quiet}")
    pass
