import logging.config
import yaml
import os
from enum import StrEnum, auto
from pathlib import Path
from dataclasses import dataclass
from configparser import ConfigParser
from importlib import resources


__all__ = [
    'NEOBASIC_HOME_PATH', 'CONFIG_FILE_PATH', 'AppConfig', 'getDefaultConfig', 'getAppConfig'
]


# ----------------------------------------------------------------------------
# APPLICATION CONFIGURATION PATHS
# ----------------------------------------------------------------------------

CONFIG_FILE = "pneo.conf"
LOG_FILE = "pneo.log"

USER_HOME_PATH = Path.home()
NEOBASIC_HOME_PATH = USER_HOME_PATH / ".neobasic"

CONFIG_FILE_PATH = NEOBASIC_HOME_PATH / CONFIG_FILE
LOG_FILE_PATH = NEOBASIC_HOME_PATH / "logs" / LOG_FILE


# ----------------------------------------------------------------------------
# APPLICATION CONFIGURATION MODEL
# ----------------------------------------------------------------------------

class LoggingLevel(StrEnum):
    DEBUG = auto()
    INFO = auto()
    WARNING = auto()
    ERROR = auto()
    CRITICAL = auto()


@dataclass
class I18nConfig:
    locale: str
    timezone: str
    date_format: str
    time_format: str
    decimal_separator: str
    thousands_separator: str
    direction: str

@dataclass
class ThemeConfig:
    title_color: str
    section_color: str
    key_color: str
    value_color: str
    debug_color: str
    info_color: str
    warning_color: str
    error_color: str
    critical_color: str
    success_color: str

@dataclass
class LoggingConfig:
    level: LoggingLevel
    filename: Path

@dataclass
class AppConfig:
    i18nConfig: I18nConfig
    themeConfig: ThemeConfig
    logConfig: LoggingConfig

    def asDict(self) -> dict:
        dict_config = {
            "i18n": {
                "locale": self.i18nConfig.locale,
                "timezone": self.i18nConfig.timezone,
                "date_format": self.i18nConfig.date_format.replace("%", "%%"),
                "time_format": self.i18nConfig.time_format.replace("%", "%%"),
                "decimal_separator": self.i18nConfig.decimal_separator,
                "thousands_separator": self.i18nConfig.thousands_separator,
                "direction": self.i18nConfig.direction,
            },
            "theme": {
                "title_color": self.themeConfig.title_color,
                "section_color": self.themeConfig.section_color,
                "key_color": self.themeConfig.key_color,
                "value_color": self.themeConfig.value_color,
                "debug_color": self.themeConfig.debug_color,
                "info_color": self.themeConfig.info_color,
                "warning_color": self.themeConfig.warning_color,
                "error_color": self.themeConfig.error_color,
                "critical_color": self.themeConfig.critical_color,
                "success_color": self.themeConfig.success_color,
            },
            "logging": {
                "level": self.logConfig.level,
                "filename": self.logConfig.filename,
            },
        }
        return dict_config


# ----------------------------------------------------------------------------
# SETTINGS HELPERS
# ----------------------------------------------------------------------------

# Read the content of a configuration file inside de project, from a module.
def read_config_resource(filename: str = CONFIG_FILE) -> str:
    content: str = None
    with resources.open_text("pneo.config", filename) as f:
        content = f.read()

    return content


# Read the content of a configuration file outside, from a OS path.
def read_config_file(file_path: Path | None) -> ConfigParser:
    config_parser = ConfigParser()

    # if exists config-file, read config from there:
    if file_path is not None and file_path.exists():
        # `read()` returns a list of files that it successfully read.
        read_files = config_parser.read(file_path)

        # We check if our file is in that list.
        if os.fspath(file_path) in read_files:
            # The file was successfully read.
            # You can now work with the config object.
            # print(f"Successfully read the file '{file_path}'.")
            return config_parser

    # no config file means, load default config.
    default_settings: str = getDefaultConfig()
    # Read the settings inside the project (default configuration).
    config_parser.read_string(default_settings)

    return config_parser


# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# first, just declare singleton instances for application settings.
default_config: str = None
app_config: AppConfig = None


def getDefaultConfig() -> str:
    global default_config
    
    # check like it is a singleton
    if default_config is None:
        # first time: load the configuration now.
        default_config = read_config_resource(CONFIG_FILE)

    return default_config


def getAppConfig() -> AppConfig:
    global app_config
    
    # check like it is a singleton
    if app_config is None:
        # first time: load the configuration now
        config_parser = read_config_file(CONFIG_FILE_PATH)

        # load the settings in the global config instance:
        i18n_config = I18nConfig(**config_parser["i18n"])
        theme_config = ThemeConfig(**config_parser["theme"])
        log_config = LoggingConfig(**config_parser["logging"])
        app_config = AppConfig(i18nConfig = i18n_config, themeConfig = theme_config, logConfig = log_config)

    return app_config


# ----------------------------------------------------------------------------
# GLOBAL LOGGING
# ----------------------------------------------------------------------------

# initialize the singleton instances.
default_config = getDefaultConfig()
app_config = getAppConfig()

log_level: str = app_config.logConfig.level
log_level = log_level.casefold() if log_level is not None else "notset"

log_config_file: str = None
match log_level:
    case "info" | "warning" | "error" | "critical":
        # this logging configuration has file:
        log_config_file = "info.yaml"

    case "debug":
        # this logging configuration has file:
        log_config_file = "debug.yaml"

    case _:
        # this logging configuration uses console, does not have file:
        log_config_file = "notset.yaml"

# load the logging configuration from inside pneo package (resource).
log_config_dict: dict = yaml.safe_load(read_config_resource(log_config_file))

if log_config_file != "notset.yaml":
    log_filename: str = app_config.logConfig.filename
    # Ensure log path directory exists in current OS.
    log_filename = os.path.expanduser(log_filename)
    os.makedirs(os.path.dirname(log_filename), exist_ok=True)

    log_config_dict["handlers"]["logfile"]["level"] = log_level.upper()
    log_config_dict["handlers"]["logfile"]["filename"] = log_filename

# as soon as the app is loaded, set the logging configuration:
logging.config.dictConfig(config=log_config_dict)
