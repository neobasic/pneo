import click

from pneo import commands
from pneo.config import create_config_file, get_config
from pneo.tracing.logger import setup_logging, logger
from pneo.tracing.strategies import InfoLoggerStrategy


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

    setup_logging(InfoLoggerStrategy())

    config = get_config()

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


def main():
    print("Hello from pneo main!")


cli.add_command(commands.config)

if __name__ == "__main__":
    main()
