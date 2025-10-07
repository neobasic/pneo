import logging
from pathlib import Path
from builtins import _, fdocstr

import pneo
from pneo.command.receiver.receiver_config import (
    create_config_file, 
    show_config_file, 
    reset_config_file,
    update_config_file,
)

import click


# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application settings.
app_config: pneo.AppConfig = pneo.getAppConfig()


# ----------------------------------------------------------------------------
# CLICK: COMMAND CONFIG
# ----------------------------------------------------------------------------

config_short_help: str = _("Operates on the current configuration, or some configuration file.")

@click.group(
    invoke_without_command=False,
    short_help=config_short_help
)
@click.pass_context
@fdocstr(config_short_help)
def config(context: click.Context) -> None:
    pass


@config.command()
@click.option(
    "--path", "-p",
    required=False,
    type=click.Path(exists=False, file_okay=True, dir_okay=True),
    help=_("Path to the config file."),
)
@click.option(
    "--force", "-f",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Ignore if config file already exists."),
)
@click.option(
    "--default_config", "-d",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Use default configuration."),
)
@click.pass_context
@fdocstr(_("Creates a new configuration file."))
def create(context: click.Context, path: Path, force: bool, default_config: bool) -> None:
    target_path: Path = pneo.CONFIG_FILE_PATH if path is None else Path(path)
    if target_path.is_dir() or target_path.suffix != ".conf":
        target_path = target_path / pneo.CONFIG_FILE
        
    if target_path.exists() and not force:
        logger.warning(_("Config file already exists at %(target_path)s."), {"target_path": target_path})
        exit(1)

    create_config_file(file_path=target_path, default_ok=default_config)


@config.command()
@click.option(
    "--path", "-p",
    required=False,
    type=click.Path(exists=True, file_okay=True, dir_okay=True),
    help=_("Path to the config file."),
)
@click.option(
    "--default_config", "-d",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Use default configuration."),
)
@click.pass_context
@fdocstr(_("Resets a configuration file, or the current configuration."))
def reset(context: click.Context, path: Path, default_config: bool) -> None:
    target_path: Path = pneo.CONFIG_FILE_PATH if path is None else Path(path)
    if target_path.is_dir() or target_path.suffix != ".conf":
        target_path = target_path / pneo.CONFIG_FILE

    if not target_path.exists():
        logger.warning(_("Config file does not exist at %(target_path)s."), {"target_path": target_path})
        exit(1)

    reset_config_file(file_path=target_path, default_ok=default_config)


@config.command()
@click.option(
    "--path", "-p",
    required=False,
    type=click.Path(exists=True, file_okay=True, dir_okay=True),
    help=_("Path to the config file."),
)
@click.option(
    "--default_config", "-d",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Displays the default configuration."),
)
@click.pass_context
@fdocstr(_("Displays the content of a configuration file, or the current configuration."))
def show(context: click.Context, path: Path | None, default_config: bool) -> None:
    target_path: Path = None
    if path is not None:
        target_path = Path(path)
        if target_path.is_dir() or target_path.suffix != ".conf":
            target_path = target_path / pneo.CONFIG_FILE
    
        if not target_path.exists():
            logger.warning(_("Config file does not exist at %(target_path)s."), {"target_path": target_path})
            exit(1)

    show_config_file(file_path=target_path, default_ok=default_config)


@config.command()
@click.option(
    "--path", "-p",
    required=False,
    type=click.Path(exists=True, file_okay=True, dir_okay=True),
    help=_("Path to the config file."),
)
@click.option(
    "--logging", "-l",
    required=False,
    type=click.Choice(["notset", "debug", "info", "warning", "error", "critical"], case_sensitive=False),
    help=_("Select the logging level."),
)
@click.option(
    "--i18n", "-i",
    required=False,
    type=click.Choice(["en", "pt"], case_sensitive=False),
    help=_("Select the locale language."),
)
@click.option(
    "--theme", "-t",
    required=False,
    type=click.Choice(["light", "dark"], case_sensitive=False),
    help=_("Select the theme colors."),
)
@click.pass_context
@fdocstr(_("Updates a configuration file with the given values of the options."))
def update(context: click.Context, path: Path | None, **kwargs: dict[str, str | int | bool | None] | None) -> None:
    target_path: Path = pneo.CONFIG_FILE_PATH if path is None else Path(path)
    if target_path.is_dir() or target_path.suffix != ".conf":
        target_path = target_path / pneo.CONFIG_FILE

    if not target_path.exists():
        logger.warning(_("Config file does not exist at %(target_path)s."), {"target_path": target_path})
        exit(1)

    updates: dict = {key: value for key, value in kwargs.items() if value is not None}

    update_config_file(target_path, updates)


@config.command()
@click.pass_context
@fdocstr(_("Displays the current configuration and system information, to help report bugs."))
def report(context: click.Context) -> None:
    # print("report: { }")
    pass
