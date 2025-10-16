import logging

from nuke import Settings

# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()


# ----------------------------------------------------------------------------
# API: COMMAND VIEW
# ----------------------------------------------------------------------------


def open_view_project(command: str, min_size: bool, resizable: bool, maximized: bool, fullscreen: bool, on_top: bool,
                      easy_drag: bool, confirm_close: bool):
    logger.debug(
        "Entering: command=%s, min_size=%s, resizable=%s, maximized=%s, fullscreen=%s, on_top=%s, easy_drag=%s, confirm_close=%s",
        command, min_size, resizable, maximized, fullscreen, on_top, easy_drag, confirm_close)

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
