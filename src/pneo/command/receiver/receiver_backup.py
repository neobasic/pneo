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
# API: COMMAND BACKUP
# ----------------------------------------------------------------------------

def backup_source_file(all_ok: bool, time_ok: bool, target_file: Path):
    logger.debug("Entering: all_ok=%s, time_ok=%s, target_file=%s", all_ok, time_ok, target_file)
    pass


def backup_source(all_ok: bool, time_ok: bool):
    logger.debug("Entering: all_ok=%s, time_ok=%s", all_ok, time_ok)
    pass

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
