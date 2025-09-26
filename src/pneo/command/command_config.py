import logging
from pathlib import Path

import click

import pneo
from pneo.config.setting.setting_facade import (
    create_config_file, 
    show_config_file, 
    reset_config_file,
    update_config_file,
)


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
@click.group(invoke_without_command=False)
def config() -> None:
    """
    Operates on the current configuration, or some configuration file.
    """
    pass


@config.command()
@click.option(
    "--path", "-p",
    required=False,
    type=click.Path(exists=False, file_okay=True, dir_okay=True),
    help="Path to the config file",
)
@click.option(
    "--force", "-f",
    required=False,
    is_flag=True,
    type=click.BOOL,
    help="Ignore if config file already exists",
    default=False,
)
@click.option(
    "--default_config", "-d",
    required=False,
    is_flag=True,
    type=click.BOOL,
    help="Use default configuration",
    default=False,
)
def create(path: Path, force: bool, default_config: bool) -> None:
    """
    Creates a new configuration file.
    """
    target_path: Path = pneo.CONFIG_FILE_PATH if path is None else Path(path)
    if target_path.is_dir() or target_path.suffix != ".conf":
        target_path = target_path / pneo.CONFIG_FILE
        
    if target_path.exists() and not force:
        logger.warning(f"Config file already exists at {target_path}")
        exit(1)

    create_config_file(file_path=target_path, default_ok=default_config)


@config.command()
@click.option(
    "--path", "-p",
    required=False,
    type=click.Path(exists=True, file_okay=True, dir_okay=True),
    help="Path to the config file",
)
@click.option(
    "--default_config", "-d",
    required=False,
    is_flag=True,
    type=click.BOOL,
    help="Use default configuration",
    default=False,
)
def reset(path: Path, default_config: bool) -> None:
    """
    Resets a configuration file, or the current configuration.
    """
    target_path: Path = pneo.CONFIG_FILE_PATH if path is None else Path(path)
    if target_path.is_dir() or target_path.suffix != ".conf":
        target_path = target_path / pneo.CONFIG_FILE

    if not target_path.exists():
        logger.warning(f"Config file does not exist at {target_path}")
        exit(1)

    reset_config_file(file_path=target_path, default_ok=default_config)


@config.command()
@click.option(
    "--path", "-p",
    required=False,
    type=click.Path(exists=True, file_okay=True, dir_okay=True),
    help="Path to the config file",
)
@click.option(
    "--default_config", "-d",
    required=False,
    is_flag=True,
    type=click.BOOL,
    help="Displays the default configuration",
    default=False,
)
def show(path: Path | None, default_config: bool) -> None:
    """
    Displays the content of a configuration file, or the current configuration.
    """
    target_path: Path = None
    if path is not None:
        target_path = Path(path)
        if target_path.is_dir() or target_path.suffix != ".conf":
            target_path = target_path / pneo.CONFIG_FILE
    
        if not target_path.exists():
            logger.warning(f"Config file does not exist at {target_path}")
            exit(1)

    show_config_file(file_path=target_path, default_ok=default_config)


@config.command()
@click.option(
    "--path", "-p",
    required=False,
    type=click.Path(exists=True, file_okay=True, dir_okay=True),
    help="Path to the config file",
)
@click.option(
    "--logging", "-l",
    required=False,
        type=click.Choice(["notset", "debug", "info", "warning", "error", "critical"], case_sensitive=False),
    help="Select the logging level: notset, debug, info, warning, error, critical",
)
@click.option(
    "--i18n", "-i",
    required=False,
    type=click.Choice(["en", "pt"], case_sensitive=False),
    help="Select the locale language: en, pt",
)
@click.option(
    "--theme", "-t",
    required=False,
    type=click.Choice(["light", "dark"], case_sensitive=False),
    help="Select the theme colors: light, dark",
)
def update(path: Path | None, **kwargs: dict[str, str | int | bool | None] | None) -> None:
    """
    Updates a configuration file with the given values of the options.
    """
    target_path: Path = pneo.CONFIG_FILE_PATH if path is None else Path(path)
    if target_path.is_dir() or target_path.suffix != ".conf":
        target_path = target_path / pneo.CONFIG_FILE

    if not target_path.exists():
        logger.warning(f"Config file does not exist at {target_path}")
        exit(1)

    updates: dict = {key: value for key, value in kwargs.items() if value is not None}

    update_config_file(target_path, updates)
