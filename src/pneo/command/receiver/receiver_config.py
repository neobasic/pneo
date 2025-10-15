import os
import logging
from pathlib import Path
from configparser import ConfigParser
from typing import Any, Optional

import click

from nuke import gettext as _, ngettext as _n, Settings, echo, p_trace, p_debug, p_info, p_warn, p_error, p_fatal


# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()


# ----------------------------------------------------------------------------
# API: COMMAND CONFIG
# ----------------------------------------------------------------------------


# create a new configuration file with default setup.
def create_config_file(file_path: Path, default_ok: bool = False):
    logger.debug("Entering: file_path=%s, default_ok=%s", file_path, default_ok)

    # Ensure config path directory exists.
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    if default_ok:
        # Read the setup inside the project (default configuration).
        default_config: str = settings.app.default_config

        # Write the setup content in config file:
        with open(file_path, "w") as f:
            f.write(default_config)
    else:
        # Use the current setup (from config file).
        config_parser: ConfigParser = ConfigParser()
        config_parser.read_dict(settings.to_dict())

        # Write the setup content in config file:
        with open(file_path, "w") as f:
            logger.debug("Creating config file at '%s'.", file_path)
            config_parser.write(f)


# Resets a config file to default configuration.
def reset_config_file(file_path: Path, default_ok: bool = False):
    logger.debug("Entering: file_path=%s, default_ok=%s", file_path, default_ok)

    if default_ok:
        # Read the setup inside the project (default configuration).
        default_config: str = settings.app.default_config

        # Write the setup content in config file:
        with open(file_path, "w") as f:
            f.write(default_config)
    else:
        # Use the current setup (from config file).
        config_parser: ConfigParser = ConfigParser()
        config_parser.read_dict(settings.to_dict())

        # Write the setup content in config file:
        with open(file_path, "w") as f:
            logger.debug("Tracing: Resetting config file at '%s'.", file_path)
            config_parser.write(f)


# Show the content of a config file, or the current setup.
def show_config_file(file_path: Optional[Path], default_ok: bool = False):
    logger.debug("Entering: file_path=%s, default_ok=%s", file_path, default_ok)

    title: str = ""
    config_parser: ConfigParser = ConfigParser()

    if default_ok:
        title = _("\nPNEO Default Configuration:")
        # Read the setup inside the project (default configuration).
        default_config: str = settings.app.default_config
        config_parser.read_string(default_config)

    elif file_path is None:
        title = _("\nPNEO Current Configuration:")
        # Use the current setup (from config file).
        config_parser.read_dict(settings.to_dict())

    else:
        title = _("\nPNEO File Configuration:")
        # Read the setup inside the file.
        config_parser.read(file_path)

    # Print the configuration
    logger.debug("Tracing: Showing config file at '%s'.", file_path)
    click.echo(click.style(title, fg=settings.theme.title_color, bold=True))
    for section in config_parser.sections():
        click.echo(
            click.style(f"\n[{section}]", fg=settings.theme.section_color, bold=True)
        )
        for key, value in config_parser.items(section):
            click.echo(
                f"  {click.style(key, fg=settings.theme.key_color)} = {click.style(str(value), fg=settings.theme.value_color)}"
            )
    click.echo()


# Update the setup of a config file, or the current config file.
def update_config_file(file_path: Path, updates: dict[str, Any]):
    logger.debug("Entering: file_path=%s, updates=%s", file_path, updates)

    config_parser: ConfigParser = ConfigParser()
    if file_path is None:
        # Use the current setup (from config file).
        config_parser.read_dict(settings.to_dict())
    else:
        # Read the setup inside the file.
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
                        config_parser.set("logging", "filename", str(settings.app.log_path))

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

    # Write the updated setup in config file:
    with open(file_path, "w") as f:
        logger.debug("Tracing: Updating config file at '%s'.", file_path)
        config_parser.write(f)


# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
