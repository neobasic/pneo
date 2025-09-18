from pathlib import Path

import click

from pneo.config import (
    CONFIG_FILE_PATH,
    Config,
    create_config_file,
    get_config,
    read_config,
    reset_config_file,
    set_config,
    update_dict,
)
from pneo.tracing.logger import logger


@click.group(invoke_without_command=False)
def config() -> None:
    pass


@config.command()
@click.option("--path",
              "-p",
              required=False,
              type=click.Path(exists=False, file_okay=True, dir_okay=False),
              help="Path to the config file",)
def create(path: Path | None) -> None:
    """
    Creates a new config file.
    """
    target_path = Path(path) if path else Path(CONFIG_FILE_PATH)

    if target_path.exists():
        logger.info(f"Config file already exists at {target_path}")
        exit(1)

    create_config_file(file_path=target_path)


@config.command()
@click.option("--path",
              "-p",
              required=False,
              type=click.Path(exists=True, file_okay=True, dir_okay=True),
              default=CONFIG_FILE_PATH,
              help="Path to the config file",)
def show(path: Path) -> None:
    """
    Displays the current config file.
    """
    target_path = Path(path) if path else Path(CONFIG_FILE_PATH)

    logger.info(f"Reading config file at {target_path}")
    read_config(file_path=target_path)


@config.command()
@click.option("--path",
              "-p",
              required=False,
              type=click.Path(exists=True, file_okay=True, dir_okay=True),
              default=CONFIG_FILE_PATH,
              help="Path to the config file",)
def reset(path: Path) -> None:
    """
    Resets the current config file to default.
    """
    target_path = Path(path) if path else Path(CONFIG_FILE_PATH)

    reset_config_file(target_path=target_path)


@config.command()
@click.option("--path",
              "-p",
              required=False,
              type=click.Path(exists=True, file_okay=True, dir_okay=True),
              default=CONFIG_FILE_PATH,)
@click.option("--min_silence_len",
              "-msl",
              required=False,
              type=click.IntRange(0, 10000),
              help="Minimum silence length in milliseconds",)
@click.option("--silence_thresh",
              "-st",
              required=False,
              type=click.IntRange(-100, 0),
              help="Silence threshold in dB",)
@click.option("--keep_silence",
              "-ks",
              required=False,
              type=click.BOOL,
              help="Keep silence",
              default=False,)
def update(path: Path, **kwargs: dict[str, str | int | bool | None] | None) -> None:
    """
    Updates the config file with the given values of the options.
    """
    target_path = Path(path) if path else Path(CONFIG_FILE_PATH)

    configur = get_config(file_path=target_path)

    if configur is None:
        logger.error("Config file not found")
        exit(1)

    updates = {key: value for key, value in kwargs.items() if value is not None}

    updated_dict = update_dict(configur.model_dump(), updates)

    updated_config = Config(**updated_dict)

    set_config(file_path=target_path, config=updated_config)

    for key, value in updates.items():
        logger.info(f"Updated {key} to {value}")
