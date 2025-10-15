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
# API: COMMAND COMPILE
# ----------------------------------------------------------------------------

def compile_files(target: Path, files: tuple[str, ...], no_warn_ok: bool):
    logger.debug("Entering: target=%s, files=%s, no_warn_ok=%s", target, files, no_warn_ok)

    pass

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
