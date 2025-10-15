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
# API: COMMAND BUILD
# ----------------------------------------------------------------------------

def build_source(source: Path, target: Path, keep_going_ok: bool) -> None:
    logger.debug("Entering: source=%s, target=%s, keep_going_ok=%s", source, target, keep_going_ok)
    pass

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
