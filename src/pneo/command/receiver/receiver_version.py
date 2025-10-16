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
# API: COMMAND VERSION
# ----------------------------------------------------------------------------


def show_project_version(manifest_file: str):
    logger.debug("Entering: manifest_file=%s", manifest_file)


def set_project_version(manifest_file: str, new_version: str, bump: str, frozen_ok: bool):
    logger.debug("Entering: manifest_file=%s, new_version=%s, bump=%s, frozen_ok=%s",
                 manifest_file, new_version, bump, frozen_ok)

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
