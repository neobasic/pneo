import sys
import logging

import click

import pneo
from pneo.command import (
    command_config,
    command_init,
    command_clean,
    command_add,
)


# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application settings.
app_config: pneo.AppConfig = pneo.getAppConfig()


# ----------------------------------------------------------------------------
# ERROR CONSTANTS
# ----------------------------------------------------------------------------

# Possible errors that may occur when executing the application to return in sys.exit():
EXIT_ERROR_CONFIG_LOG = -1
EXIT_ERROR_CONFIG_APP = -2
EXIT_ERROR_INVALID_ARGS = -3
EXIT_ERROR_NO_ARGS = -4
EXIT_ERROR_MAIN = "Module '__main__.py' cannot be loaded by another module!"
# EXIT_ERROR_MAIN = "O modulo '__main__.py' nao pode ser carregado por outro modulo!"

EXIT_SUCCESS = 0  # informs that in fact no error occurred, it was executed successfully.


# ----------------------------------------------------------------------------
# ENTRY-POINT CHECK
# ----------------------------------------------------------------------------

# This module cannot be loaded by another module
if __name__ not in ["__main__", "pneo.__main__"]:
    sys.exit(EXIT_ERROR_MAIN)
# proceeds only if this program was executed as entry-point...


# ----------------------------------------------------------------------------
# MAIN ENTRY-POINT
# ----------------------------------------------------------------------------

# Adds the option '-h' for help.
CONTEXT_SETTINGS: dict = dict(help_option_names=["-h", "--help"])

@click.group(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.version_option()
def cli(context: click.Context) -> None:
    """
    Pneo is a tool ...

    In order to use Pneo, ... as an option. Or alternativly,
    as an enviroment variable in the current session.
    """

    # setting = get_config()
    # # setup_logging(DevLoggerStrategy(), setting["logging"]["filename"])

    # if setting is None and context.invoked_subcommand == "setting":
    #     logger.info("Config file not found")
    #     create_config_file()
    #     exit(0)

    # if setting is None:
    #     logger.error("Config file not found")
    #     logger.info("Run the following command to create a new setting file: `pneo setting create`")
    #     exit(1)

    context.ensure_object(dict)
    if not context.invoked_subcommand == "setting":
        context.obj["parser"] = None

    context.obj["setting"] = app_config


# ----------------------------------------------------------------------------
# CLICK: COMMAND LINE ARGUMENTS
# ----------------------------------------------------------------------------

# 
cli.add_command(command_config.config)
cli.add_command(command_init.init)
cli.add_command(command_clean.clean)
cli.add_command(command_add.add)
cli()
