import logging
from enum import StrEnum, auto
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
# API: COMMAND INIT
# ----------------------------------------------------------------------------


class ProjectType(StrEnum):
    APP = auto()
    LIB = auto()


def initialize_project(name: str, path: Path, ptype: ProjectType):
    logger.debug("Entering: name=%s, path=%s, ptype=%s", name, path, ptype)
    pass

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
