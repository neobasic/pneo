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
# API: COMMAND VENV
# ----------------------------------------------------------------------------

def create_venv_path(venv_dir: str, check_ok: bool, sync_ok: bool, locked_ok: bool):
    logger.debug("Entering: venv_dir=%s, check_ok=%s, sync_ok=%s, locked_ok=%s", venv_dir, check_ok, sync_ok, locked_ok)

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
