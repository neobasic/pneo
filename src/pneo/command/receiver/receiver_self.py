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
# API: COMMAND SELF
# ----------------------------------------------------------------------------


def show_pneo_version(short_ok: bool):
    logger.debug("Entering: short_ok=%s", short_ok)


def upgrade_pneo_version(target_version: str):
    logger.debug("Entering: target_version=%s", target_version)


def upgrade_pneo_latest():
    logger.debug("Entering: ...")


def uninstall_pneo(assume_yes: bool):
    logger.debug("Entering: assume_yes=%s", assume_yes)

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
