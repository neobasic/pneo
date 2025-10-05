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
# CLICK: COMMAND LOCK
# ----------------------------------------------------------------------------

view_short_help: str = _("Open a window (using native webview) to manage the project, and select the <COMMAND> tab; defaults to `home` if not provided.")

@click.command(
    options_metavar=_("<OPTIONS>"),
    short_help=view_short_help
)
@click.option(
    "--min-size", "-m",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Use minimum allowed window size."),
)
@click.option(
    "--resizable", "-r",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Whether the window can be resized by the user."),
)
@click.option(
    "--maximized", "-x",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Show window initially maximized."),
)
@click.option(
    "--fullscreen", "-f",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Start the window in fullscreen mode."),
)
@click.option(
    "--on-top", "-t",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Keeps window always on top."),
)
@click.option(
    "--easy-drag", "-d",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Whether you can drag the window by clicking anywhere."),
)
@click.option(
    "--confirm-close", "-c",
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
    metavar=_("<COMMAND>")
)
@click.pass_context
@fdocstr(view_short_help)
def view(context: click.Context, min_size: bool, resizable: bool, maximized: bool, fullscreen: bool, on_top: bool,  easy_drag: bool, confirm_close: bool, command: str) -> None:
    # print(f"min_size: {min_size}, resizable: {resizable}, maximized: {maximized}, fullscreen: {fullscreen}, on_top: {on_top}, easy_drag: {easy_drag}, confirm_close: {confirm_close}, command: {command}")
    pass
