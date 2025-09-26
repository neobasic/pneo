from abc import ABC, abstractmethod
from importlib import resources
from pathlib import Path
import logging
import logging.config

import yaml


# ----------------------------------------------------------------------------
# LOGGING STRATEGIES
# ----------------------------------------------------------------------------
class LoggerStrategy(ABC):
    @abstractmethod
    def setup_logging(self):
        pass


class InfoLoggerStrategy(LoggerStrategy):
    def setup_logging(self, log_path: Path):
        with resources.open_text("pneo.config", "info.yaml") as f:
            logging_config = yaml.safe_load(f.read())

        logging_config["handlers"]["logfile"]["filename"] = log_path
        logging.config.dictConfig(config=logging_config)


class DebugLoggerStrategy(LoggerStrategy):
    def setup_logging(self, log_path: Path):
        with resources.open_text("pneo.config", "debug.yaml") as f:
            logging_config = yaml.safe_load(f.read())

        logging_config["handlers"]["logfile"]["filename"] = log_path
        logging.config.dictConfig(config=logging_config)
