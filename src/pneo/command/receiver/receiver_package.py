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
# API: COMMAND PACKAGE
# ----------------------------------------------------------------------------

def package_binary(dist_path: Path, bin_path: Optional[Path], no_warn_ok: bool):
    logger.debug("Entering: dist_path=%s, bin_path=%s, no_warn_ok=%s", dist_path, bin_path, no_warn_ok)

    pass

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
