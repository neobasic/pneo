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
# API: COMMAND HOTSPOT
# ----------------------------------------------------------------------------

def start_hotspot(source: Path, target: Path, no_warn_ok: bool) -> None:
    logger.debug("Entering: source=%s, target=%s, no_warn_ok=%s", source, target, no_warn_ok)
    pass

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
