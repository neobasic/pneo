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
# API: COMMAND PARSE
# ----------------------------------------------------------------------------

def parse_file(file_path: Path, depth: int, all_info_ok: bool, short_ok: bool):
    logger.debug("Entering: file_path=%s, depth=%s, all_info_ok=%s, short_ok=%s",
                 file_path, depth, all_info_ok, short_ok)

    pass

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
