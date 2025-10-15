import logging
from pathlib import Path

from nuke import gettext as _, ngettext as _n, Settings, echo, p_trace, p_debug, p_info, p_warn, p_error, p_fatal


# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()


# ----------------------------------------------------------------------------
# API: COMMAND MAKE
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
