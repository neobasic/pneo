import os
import yaml
import logging.config
import gettext
import locale
import builtins
from typing import Sequence, Optional, Dict, List, AnyStr
from pathlib import Path
from importlib import resources
from enum import StrEnum, auto
from dataclasses import dataclass
from configparser import ConfigParser


__all__ = [
    'NEOBASIC_HOME_PATH', 'CONFIG_FILE_PATH', 'AppConfig', 'getDefaultConfig', 'getAppConfig'
]


# ----------------------------------------------------------------------------
# APPLICATION CONFIGURATION PATHS
# ----------------------------------------------------------------------------

APP_MODULE: str = "pneo"
APP_DOMAIN: str = APP_MODULE

CONFIG_FILE = APP_DOMAIN + ".conf"
LOG_FILE = APP_DOMAIN + ".log"

USER_HOME_PATH = Path.home()
NEOBASIC_HOME_PATH = USER_HOME_PATH / ".neobasic"

# check if user declared a environment variable NEOBASIC_HOME.
envar_neobasic_home = os.getenv("NEOBASIC_HOME")
if envar_neobasic_home is not None:
    envar_path = Path(envar_neobasic_home)
    if envar_path.exists():
        NEOBASIC_HOME_PATH = envar_path

# whenever possible, uses envar NEOBASIC_HOME first.
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
    locale: AnyStr
    timezone: AnyStr
    date_format: AnyStr
    time_format: AnyStr
    decimal_separator: AnyStr
    thousands_separator: AnyStr
    direction: AnyStr

@dataclass
class ThemeConfig:
    title_color: AnyStr
    section_color: AnyStr
    key_color: AnyStr
    value_color: AnyStr
    debug_color: AnyStr
    info_color: AnyStr
    warning_color: AnyStr
    error_color: AnyStr
    critical_color: AnyStr
    success_color: AnyStr

@dataclass
class LoggingConfig:
    level: LoggingLevel
    filename: Path

@dataclass
class AppConfig:
    i18nConfig: I18nConfig
    themeConfig: ThemeConfig
    logConfig: LoggingConfig

    def asDict(self) -> Dict:
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

# Read the content of a configuration file inside the project, from a module.
def read_config_resource(filename: AnyStr = CONFIG_FILE) -> AnyStr:
    content: AnyStr = None
    with resources.open_text(CONFIG_FILE, filename) as f:
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
            return config_parser

    # no config file means, load default config.
    default_settings: AnyStr = getDefaultConfig()
    # Read the settings inside the project (default configuration).
    config_parser.read_string(default_settings)

    return config_parser


# decorator to patch the docstring of a function, to enable
# the use of gettext '_' in a docstring before the click library.
def fdocstr(docstr: AnyStr):
    def wrapper(func):
        func.__doc__ = docstr
        return func
    return wrapper

# put the decorator in the global scope for all modules.
builtins.__dict__['fdocstr'] = fdocstr


# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# first, just declare singleton instances for application settings.
default_config: AnyStr = None
app_config: AppConfig = None


def getDefaultConfig() -> AnyStr:
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
        if log_config.filename == "None":  # Just to be sure it did not set None as string.
            log_config.filename = None
        app_config = AppConfig(i18nConfig = i18n_config, themeConfig = theme_config, logConfig = log_config)

    return app_config


# then, initialize the singleton instances.
default_config = getDefaultConfig()
app_config = getAppConfig()


# ----------------------------------------------------------------------------
# GLOBAL LOGGING
# ----------------------------------------------------------------------------

log_level: AnyStr = app_config.logConfig.level
log_level = log_level.casefold() if log_level is not None else "notset"

log_config_file: AnyStr = None
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

# load the logging configuration from inside the app packages (resource).
log_config_dict: Dict = yaml.safe_load(read_config_resource(log_config_file))

if log_config_file != "notset.yaml":
    log_filename: str = LOG_FILE_PATH
    if app_config.logConfig.filename is not None:
        log_filename = app_config.logConfig.filename
    # Ensure log path directory exists in current OS.
    log_filename = os.path.expanduser(log_filename)
    os.makedirs(os.path.dirname(log_filename), exist_ok=True)

    log_config_dict["handlers"]["logfile"]["level"] = log_level.upper()
    log_config_dict["handlers"]["logfile"]["filename"] = log_filename

# as soon as the app is loaded, set the logging configuration:
logging.config.dictConfig(config=log_config_dict)


# ----------------------------------------------------------------------------
# GLOBAL INTERNATIONALIZATION (I18N) & LOCALIZATION (L10N)  
# ----------------------------------------------------------------------------

VALID_LOCALES: List = ['en_US', 'pt_BR']
DEFAULT_LOCALE: AnyStr = 'en_US'  # fallback language.

# check the configured locale language:
lang: AnyStr = app_config.i18nConfig.locale
if lang not in VALID_LOCALES:
    # get the default locale already configured of OS.
    locale.setlocale(locale.LC_ALL, '')
    lang, _ = locale.getlocale()
    if lang not in VALID_LOCALES:
        lang = DEFAULT_LOCALE

# configure the choosen locale as global locale:
value_locale: AnyStr = lang + ".UTF-8"
locale.setlocale(locale.LC_ALL, value_locale)

# include the default-locale at the end, as a fallback.
languages: List = [lang]
if DEFAULT_LOCALE not in languages:
    languages.append(DEFAULT_LOCALE)

# path to the locale folder (defaults to src/app/locale, or relative to this file)
heredir = os.path.abspath(os.path.dirname(__file__))
localedir = os.path.normpath(os.path.join(heredir, "locale"))

# fallback=True avoids exceptions if any file .mo is missing.
domain_translations = gettext.translation(APP_DOMAIN, localedir=localedir, languages=languages, fallback=True)
click_translations = gettext.translation("click", localedir=localedir, languages=languages, fallback=True)

# If a string isn’t found in 'messages.po', gettext looks in the fallback ('click').
domain_translations.add_fallback(click_translations)

# Install gettext('_') into builtins for the chosen domain and localedir.
domain_translations.install()   # registers builtin _() and ngettext() globally.
