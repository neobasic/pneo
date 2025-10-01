import os
import logging
from pathlib import Path
from builtins import _

import click

import pneo


# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application settings.
app_config: pneo.AppConfig = pneo.getAppConfig()


# ----------------------------------------------------------------------------
# API: COMMAND MAKE
# ----------------------------------------------------------------------------



# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
