import logging

import click
from nuke import gettext as _, Settings, fdocstr
from nuke.formatters.print_color import p_error
from pneo.command.receiver.receiver_serve import start_lsp_socket, start_lsp_stdio

# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()

# ----------------------------------------------------------------------------
# CLICK: COMMAND SERVE
# ----------------------------------------------------------------------------

_serve_short_help: str = _("Run in language server mode, ready to handle requests from a client (the editor).")


@click.command(options_metavar=_("<OPTIONS>"), short_help=_serve_short_help)
@click.option(
    "--stdio",
    "-s",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_(
        "Instructs the server to communicate over its standard input (stdin) and standard output (stdout)."
    ),
)
@click.option(
    "--socket-port",
    "-p",
    required=False,
    type=click.IntRange(0, 65535, clamp=True),
    help=_(
        "Instructs the server to listen on a specific TCP port for a client connection (socket). Used for remote development, servers running as persistent services, or clients that prefer TCP, often enabling multiple clients to connect to a single server instance."
    ),
)
@click.option(
    "--limit-results",
    "-l",
    required=False,
    type=click.IntRange(1, 100, clamp=True),
    default=10,
    help=_("Limit completion items. [default: 10]"),
)
@click.option(
    "--noisy",
    "-n",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Increases the server's logging and output verbosity."),
)
@click.option(
    "--quiet",
    "-q",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Decreases the server's logging and output verbosity (opposite of verbose)."),
)
@click.pass_context
@fdocstr(_serve_short_help)
def serve(context: click.Context, stdio: bool, socket_port: int, limit_results: int, noisy: bool, quiet: bool) -> None:
    logger.debug("Entering: stdio=%s, socket_port=%s, limit_results=%s, noisy=%s, quiet=%s",
                 stdio, socket_port, limit_results, noisy, quiet)

    # can't use --stdio and --socket-port together.
    if stdio and socket_port:
        logger.error("Used both options '--stdio' and '--socket-port' in command SERVE.")
        p_error(_("Error: The flags <*'--stdio'*> and <*'--socket-port'*> are mutually exclusive; choose only one."))
        exit(1)

    elif stdio:
        # proceed with starting the language server in stdio mode.
        start_lsp_stdio(limit_results, noisy, quiet)

    else:
        # proceed with starting the language server in socket mode.
        start_lsp_socket(socket_port, limit_results, noisy, quiet)
