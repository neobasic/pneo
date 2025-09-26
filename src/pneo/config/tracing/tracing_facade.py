import logging
import logging.config

from pneo.config.tracing.strategies import LoggerStrategy


# ----------------------------------------------------------------------------
# LOGGING CONFIGURATION API
# ----------------------------------------------------------------------------

# logger = logging.getLogger("root")

def setup_logging(strategy: LoggerStrategy) -> None:
    strategy.setup_logging()
