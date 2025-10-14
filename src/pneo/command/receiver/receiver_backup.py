import os
import logging
from pathlib import Path
from typing import Optional

from nuke import gettext as _, ngettext as _n, AppConfig, echo, p_trace, p_debug, p_info, p_warn, p_error, p_fatal


# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application settings.
app_config: AppConfig = AppConfig.get_instance()


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
