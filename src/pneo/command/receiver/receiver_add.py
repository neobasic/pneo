import logging
from pathlib import Path
from enum import StrEnum, auto

from nuke import gettext as _, ngettext as _n, Settings, echo, p_trace, p_debug, p_info, p_warn, p_error, p_fatal


# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()


# ----------------------------------------------------------------------------
# API: COMMAND ADD
# ----------------------------------------------------------------------------


class LibraryLinking(StrEnum):
    STATIC = auto()
    DYNAMIC = auto()


def add_dependency_web(packages: tuple, linking: LibraryLinking) -> None:
    logger.debug("Entering: packages=%s, linking=%s", packages, linking)
    pass


def add_dependency_path(dep_path: Path, packages: tuple, linking: LibraryLinking) -> None:
    logger.debug("Entering: dep_path=%s, packages=%s, linking=%s", dep_path, packages, linking)
    pass


# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
