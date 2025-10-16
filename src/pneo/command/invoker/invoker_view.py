import logging

import click
from nuke import gettext as _, Settings, fdocstr
from pneo.command.receiver.receiver_view import open_view_project

# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()

# ----------------------------------------------------------------------------
# CLICK: COMMAND VIEW
# ----------------------------------------------------------------------------

_view_short_help: str = _(
    "Open a window (using native webview) to manage the project, and select the <COMMAND> tab; defaults to `home` if not provided.")


@click.command(options_metavar=_("<OPTIONS>"), short_help=_view_short_help)
@click.option(
    "--min-size",
    "-m",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Use minimum allowed window size."),
)
@click.option(
    "--resizable",
    "-r",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Whether the window can be resized by the user."),
)
@click.option(
    "--maximized",
    "-x",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Show window initially maximized."),
)
@click.option(
    "--fullscreen",
    "-f",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Start the window in fullscreen mode."),
)
@click.option(
    "--on-top",
    "-t",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Keeps window always on top."),
)
@click.option(
    "--easy-drag",
    "-d",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Whether you can drag the window by clicking anywhere."),
)
@click.option(
    "--confirm-close",
    "-c",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Whether to ask confirmation before closing."),
)
@click.argument(
    "command",
    required=False,
    type=click.STRING,
    metavar=_("<COMMAND>"),
)
@click.pass_context
@fdocstr(_view_short_help)
def view(context: click.Context, min_size: bool, resizable: bool, maximized: bool, fullscreen: bool, on_top: bool,
         easy_drag: bool, confirm_close: bool, command: str) -> None:
    logger.debug(
        "Entering: min_size=%s, resizable=%s, maximized=%s, fullscreen=%s, on_top=%s, easy_drag=%s, confirm_close=%s, command=%s",
        min_size, resizable, maximized, fullscreen, on_top, easy_drag, confirm_close, command)

    # proceed with the opening of window to view/maintain the project.
    open_view_project(command, min_size, resizable, maximized, fullscreen, on_top, easy_drag, confirm_close)
