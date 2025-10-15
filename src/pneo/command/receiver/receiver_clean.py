import logging
from pathlib import Path

from nuke import Settings

# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()


# ----------------------------------------------------------------------------
# API: COMMAND CLEAN
# ----------------------------------------------------------------------------

def clean_project_path(dir_path: Path, assume_yes_ok: bool):
    logger.debug("Entering: dir_path=%s, assume_yes_ok=%s", dir_path, assume_yes_ok)


def clean_project(assume_yes: bool):
    logger.debug("Entering: assume_yes=%s", assume_yes)

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
