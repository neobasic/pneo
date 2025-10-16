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
# API: COMMAND TREE
# ----------------------------------------------------------------------------


def display_dependency_tree(manifest_file: str, depth: int, outdated_ok: bool, show_sizes_ok: bool):
    logger.debug("Entering: manifest_file=%s, depth=%s, outdated_ok=%s, show_sizes_ok=%s",
                 manifest_file, depth, outdated_ok, show_sizes_ok)

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
