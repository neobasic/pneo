import logging

from nuke import Settings

# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()


# ----------------------------------------------------------------------------
# API: COMMAND LOCK
# ----------------------------------------------------------------------------

def lock_project(check_ok: bool, upgrade_ok: bool):
    logger.debug("Entering: check_ok=%s, upgrade_ok=%s", check_ok, upgrade_ok)

    pass

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
