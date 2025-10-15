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
# API: COMMAND LIST
# ----------------------------------------------------------------------------

def list_source_units(module: str, absolute_path_ok: bool, only_modules_ok: bool, long_table_ok: bool):
    logger.debug("Entering: module=%s, absolute_path_ok=%s, only_modules_ok=%s, long_table_ok=%s",
                 module, absolute_path_ok, only_modules_ok, long_table_ok)

    pass

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
