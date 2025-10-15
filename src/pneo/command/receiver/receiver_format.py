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
# API: COMMAND FORMAT
# ----------------------------------------------------------------------------

def format_files(files: tuple[str, ...], keep_going_ok: bool, diff_ok: bool):
    logger.debug("Entering: files=%s, keep_going_ok=%s, diff_ok=%s", files, keep_going_ok, diff_ok)

    pass

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
