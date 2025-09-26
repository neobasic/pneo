import os
from configparser import ConfigParser
from pathlib import Path
from typing import Any
import logging

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
# APPLICATION SETTINGS API
# ----------------------------------------------------------------------------

# create a new configuration file with default settings.
def create_config_file(file_path: Path, default_ok: bool = False):
    logger.debug(f"Creating config file at: {file_path}")

    # Ensure config path directory exists.
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    if default_ok:
        # Read the settings inside the project (default configuration).
        content_str: str = pneo.read_config_resource()

        # Write the settings content in config file:
        with open(file_path, "w") as f:
            f.write(content_str)
    else:
        # Use the current settings (from config file).
        config_parser: ConfigParser = ConfigParser()
        config_parser.read_dict(app_config.asDict())

        # Write the settings content in config file:
        with open(file_path, "w") as f:
            config_parser.write(f)


# Resets a config file to default configuration.
def reset_config_file(file_path: Path, default_ok: bool = False):
    logger.debug(f"Resetting config file at: {file_path}")

    if default_ok:
        # Read the settings inside the project (default configuration).
        content_str: str = pneo.read_config_resource()

        # Write the settings content in config file:
        with open(file_path, "w") as f:
            f.write(content_str)
    else:
        # Use the current settings (from config file).
        config_parser: ConfigParser = ConfigParser()
        config_parser.read_dict(app_config.asDict())

        # Write the settings content in config file:
        with open(file_path, "w") as f:
            config_parser.write(f)


# Show the content of a config file, or the current settings.
def show_config_file(file_path: Path | None, default_ok: bool = False):
    logger.debug(f"Showing config file at: {file_path}")

    title: str = None
    config_parser: ConfigParser = ConfigParser()

    if default_ok:
        title = "\nPNEO Default Configuration:"
        # Read the settings inside the project (default configuration).
        content_str: str = pneo.read_config_resource()
        config_parser.read_string(content_str)
    elif file_path is None:
        title = "\nPNEO Current Configuration:"
        # Use the current settings (from config file).
        config_parser.read_dict(app_config.asDict())
    else:
        title = "\nPNEO File Configuration:"
        # Read the settings inside the file.
        config_parser.read(file_path)

    # Print the configuration
    click.echo(click.style(title, fg=app_config.themeConfig.title_color, bold=True))
    for section in config_parser.sections():
        click.echo(click.style(f"\n[{section}]", fg=app_config.themeConfig.section_color, bold=True))
        for key, value in config_parser.items(section):
            click.echo(f"  {click.style(key, fg=app_config.themeConfig.key_color)} = {click.style(str(value), fg=app_config.themeConfig.value_color)}")
    click.echo()


# Update the settings of a config file, or the current config file.
def update_config_file(file_path: Path, updates: dict[str, Any]):
    logger.debug(f"Updating config file at: {file_path}")

    config_parser: ConfigParser = ConfigParser()
    if file_path is None:
        # Use the current settings (from config file).
        config_parser.read_dict(app_config.asDict())
    else:
        # Read the settings inside the file.
        config_parser.read(file_path)

    # apply the updates in config data structure.
    for key, value in updates.items():
        match key:
            case "logging":
                config_parser.set("logging", "level", str(value))
                # automatically configures the other logging options.
                match str(value).casefold():
                    case "notset":
                        config_parser.set("logging", "filename", "None")

                    case "debug" | "info" | "warning" | "error" | "critical":
                        config_parser.set("logging", "filename", str(pneo.LOG_FILE_PATH))

            case "i18n":
                # automatically configures all the other i18n options.
                match str(value).casefold():
                    case "en":
                        config_parser.set("i18n", "locale", "en_US")
                        config_parser.set("i18n", "timezone", "America/New_York")
                        config_parser.set("i18n", "date_format", "%%m/%%d/%%Y")
                        config_parser.set("i18n", "time_format", "%%I:%%M:%%S %%p")
                        config_parser.set("i18n", "decimal_separator", ".")
                        config_parser.set("i18n", "thousands_separator", ",")
                        config_parser.set("i18n", "direction", "ltr")

                    case "pt":
                        config_parser.set("i18n", "locale", "pt_BR")
                        config_parser.set("i18n", "timezone", "America/Sao_Paulo")
                        config_parser.set("i18n", "date_format", "%%d/%%m/%%Y")
                        config_parser.set("i18n", "time_format", "%%H:%%M:%%S")
                        config_parser.set("i18n", "decimal_separator", ",")
                        config_parser.set("i18n", "thousands_separator", ".")
                        config_parser.set("i18n", "direction", "ltr")

            case "theme":
                # automatically configures all the other theme options.
                match str(value).casefold():
                    case "light":
                        # TODO: Must define better color for light theme.
                        config_parser.set("theme", "title_color", "blue")
                        config_parser.set("theme", "section_color", "cyan")
                        config_parser.set("theme", "key_color", "yellow")
                        config_parser.set("theme", "value_color", "green")
                        config_parser.set("theme", "debug_color", "gray")
                        config_parser.set("theme", "info_color", "blue")
                        config_parser.set("theme", "warning_color", "yellow")
                        config_parser.set("theme", "error_color", "red")
                        config_parser.set("theme", "critical_color", "red")
                        config_parser.set("theme", "success_color", "bright_green")

                    case "dark":
                        # TODO: Must refine better color for dark theme.
                        config_parser.set("theme", "title_color", "blue")
                        config_parser.set("theme", "section_color", "cyan")
                        config_parser.set("theme", "key_color", "yellow")
                        config_parser.set("theme", "value_color", "green")
                        config_parser.set("theme", "debug_color", "gray")
                        config_parser.set("theme", "info_color", "blue")
                        config_parser.set("theme", "warning_color", "yellow")
                        config_parser.set("theme", "error_color", "red")
                        config_parser.set("theme", "critical_color", "red")
                        config_parser.set("theme", "success_color", "bright_green")

    # Write the updated settings in config file:
    with open(file_path, "w") as f:
        config_parser.write(f)


# ----------------------------------------------------------------------------
# SETTINGS HELPERS
# ----------------------------------------------------------------------------
