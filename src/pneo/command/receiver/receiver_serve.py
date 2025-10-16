import logging
from enum import StrEnum, auto

from nuke import Settings

# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()


# ----------------------------------------------------------------------------
# API: COMMAND SERVE
# ----------------------------------------------------------------------------

class ServerMode(StrEnum):
    STDIO = auto()
    SOCKET = auto()


def start_lsp_stdio(limit_results: int, noisy_ok: bool, quiet_ok: bool):
    logger.debug("Entering: limit_results=%s, noisy_ok=%s, quiet_ok=%s",
                 limit_results, noisy_ok, quiet_ok)


def start_lsp_socket(socket_port: int, limit_results: int, noisy_ok: bool, quiet_ok: bool):
    logger.debug("Entering: socket_port=%s, limit_results=%s, noisy_ok=%s, quiet_ok=%s",
                 socket_port, limit_results, noisy_ok, quiet_ok)

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
