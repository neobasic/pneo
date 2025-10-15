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
# API: COMMAND LINT
# ----------------------------------------------------------------------------


def lint_file(file: Path, keep_going_ok: bool):
    logger.debug("Entering: file=%s, keep_going_ok=%s", file, keep_going_ok)

    pass

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
