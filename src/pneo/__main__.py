import sys
import logging

import click

from pneo.command import command_config
from pneo.config import get_config, create_config_file
from pneo.tracing.logger import setup_default_logging, setup_logging
from pneo.tracing.strategies import DevLoggerStrategy


# ----------------------------------------------------------------------------
# ERROR CONSTANTS
# ----------------------------------------------------------------------------
# Possible errors that may occur when executing the application to return in sys.exit():
EXIT_ERROR_CONFIG_LOG = -1
EXIT_ERROR_CONFIG_APP = -2
EXIT_ERROR_INVALID_ARGS = -3
EXIT_ERROR_NO_ARGS = -4
EXIT_ERROR_MAIN = "O modulo '__main__.py' nao pode ser carregado por outro modulo!"

EXIT_SUCCESS = 0  # informs that in fact no error occurred, it was executed successfully.


# ----------------------------------------------------------------------------
# ENTRY-POINT CHECK
# ----------------------------------------------------------------------------
# This module cannot be loaded by another module
if __name__ not in ["__main__", "pneo.__main__"]:
    sys.exit(EXIT_ERROR_MAIN)
# proceeds only if this program was executed as entry-point...


# ----------------------------------------------------------------------------
# SETUP DEFAULT LOGGING
# ----------------------------------------------------------------------------
# check if managed to configure the default logging configuration:
if not setup_default_logging():
    print("Erro: Não foi possível configurar o logging da aplicação...")
    sys.exit(EXIT_ERROR_CONFIG_LOG)  # nao ha porque prosseguir...

# gets a logger instance for the current module:
logger = logging.getLogger(__name__)


# ----------------------------------------------------------------------------
# SETUP APPLICATION CONFIGURATION
# ----------------------------------------------------------------------------
configer = get_config()



# ----------------------------------------------------------------------------
# CLICK: COMMAND LINE ARGUMENTS
# ----------------------------------------------------------------------------
# Adds the option '-h' for help.
CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

@click.group(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.version_option()
def cli(context: click.Context) -> None:
    """
    Pneo is a tool ...

    In order to use Pneo, ... as an option. Or alternativly,
    as an enviroment variable in the current session.
    """

    config = get_config()
    # setup_logging(DevLoggerStrategy(), config["logging"]["filename"])

    if config is None and context.invoked_subcommand == "config":
        logger.info("Config file not found")
        create_config_file()
        exit(0)

    if config is None:
        logger.error("Config file not found")
        logger.info("Run the following command to create a new config file: `pneo config create`")
        exit(1)

    context.ensure_object(dict)
    if not context.invoked_subcommand == "config":
        context.obj["parser"] = None

    context.obj["config"] = config


# ----------------------------------------------------------------------------
# MAIN ENTRY-POINT
# ----------------------------------------------------------------------------
#
cli.add_command(command_config.config)
cli()
