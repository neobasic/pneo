import logging
from pathlib import Path
from typing import Optional

from nuke import Settings

# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()


# ----------------------------------------------------------------------------
# API: COMMAND RUN
# ----------------------------------------------------------------------------


def run_target(target: Path, offline_ok: bool):
    logger.debug("Entering: target=%s, offline_ok=%s", target, offline_ok)

    pass


def run_script(target: Optional[Path], script: Path, offline_ok: bool):
    logger.debug("Entering: target=%s, script=%s, offline_ok=%s", target, script, offline_ok)

    pass

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
