import os
import yaml
import logging.config
import gettext
import locale
import builtins
from typing import Sequence, Optional, Dict, List
from pathlib import Path
from importlib import resources
from enum import StrEnum, auto
from dataclasses import dataclass
from configparser import ConfigParser
from platformdirs import user_config_path, user_log_path


__all__ = [
    'USER_HOME_PATH', 'NEOBASIC_HOME_PATH', 'CONFIG_FILE_PATH', 'AppConfig', 'getAppConfig'
]


# ----------------------------------------------------------------------------
# APPLICATION SETTINGS AND CONFIGURATION PATHS
# ----------------------------------------------------------------------------

APP_DOMAIN: str = "pneo"
APP_MAIN_MODULE: str = APP_DOMAIN
APP_ANCHOR_CONFIG: str = APP_MAIN_MODULE + ".config"

CONFIG_FILE: str = APP_DOMAIN + ".conf"
CONFIG_FILE_PATH: Path = user_config_path(appname=APP_DOMAIN) / CONFIG_FILE

LOG_FILE: str = APP_DOMAIN + ".log"
LOG_FILE_PATH: Path = user_log_path(appname=APP_DOMAIN) / LOG_FILE

# just convention, where it should be.
USER_HOME_PATH: Path = Path.home()
NEOBASIC_HOME_PATH: Path = USER_HOME_PATH / ".neobasic"

# check if user declared a environment variable NEOBASIC_HOME.
envar_neobasic_home = os.getenv("NEOBASIC_HOME")
if envar_neobasic_home is not None:
    NEOBASIC_HOME_PATH = Path(envar_neobasic_home)
    if not NEOBASIC_HOME_PATH.exists():
        os.makedirs(NEOBASIC_HOME_PATH, exist_ok=True)

    # whenever possible, uses envar NEOBASIC_HOME for all tools.
    CONFIG_FILE_PATH = NEOBASIC_HOME_PATH / CONFIG_FILE
    LOG_FILE_PATH = NEOBASIC_HOME_PATH / "logs" / LOG_FILE


# ----------------------------------------------------------------------------
# APPLICATION CONFIGURATION MODEL
# ----------------------------------------------------------------------------

class LoggingLevel(StrEnum):
    NOTSET = auto()
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
    filename: str

@dataclass
class AppConfig:
    i18nConfig: I18nConfig
    themeConfig: ThemeConfig
    logConfig: LoggingConfig

    def asDict(self) -> Dict:
        print("logConfig.filename = ", self.logConfig.filename)
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
def read_config_resource(filename: str) -> str:
    content: str = None
    with resources.open_text(APP_ANCHOR_CONFIG, filename) as f:
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
    default_settings: str = getDefaultConfig()
    # Read the settings inside the project (default configuration).
    config_parser.read_string(default_settings)

    return config_parser


# decorator to patch the docstring of a function, to enable
# the use of gettext '_' in a docstring before the click library.
def fdocstr(docstr: str):
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


# then, initialize the singleton instances.
default_config = getDefaultConfig()
app_config = getAppConfig()


# ----------------------------------------------------------------------------
# GLOBAL LOGGING
# ----------------------------------------------------------------------------

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

# load the logging configuration from inside the app packages (resource).
log_config_dict: Dict = yaml.safe_load(read_config_resource(log_config_file))

if log_config_file != "notset.yaml":
    log_filename: str = LOG_FILE_PATH  # default value
    if app_config.logConfig.filename and app_config.logConfig.filename != "None":
        # just in case there is '~' in file path.
        log_filename = os.path.expanduser(app_config.logConfig.filename)
    # Ensure log path directory exists in current OS.
    os.makedirs(os.path.dirname(log_filename), exist_ok=True)

    log_config_dict["handlers"]["logfile"]["level"] = log_level.upper()
    log_config_dict["handlers"]["logfile"]["filename"] = log_filename

# as soon as the app is loaded, set the logging configuration:
logging.config.dictConfig(config=log_config_dict)


# ----------------------------------------------------------------------------
# GLOBAL INTERNATIONALIZATION (I18N) & LOCALIZATION (L10N)  
# ----------------------------------------------------------------------------

VALID_LOCALES: List = ['pt_BR', 'en_US']
DEFAULT_LOCALE: str = 'en_US'  # fallback language.

# check the configured locale language:
lang: str = app_config.i18nConfig.locale
if lang not in VALID_LOCALES:
    # get the default locale already configured of OS.
    locale.setlocale(locale.LC_ALL, '')
    lang, _ = locale.getlocale()
    if lang not in VALID_LOCALES:
        lang = DEFAULT_LOCALE

# configure the choosen locale as global locale:
value_locale: str = lang + ".UTF-8"
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
ngne_translations = gettext.translation("ngne", localedir=localedir, languages=languages, fallback=True)
click_translations = gettext.translation("click", localedir=localedir, languages=languages, fallback=True)

# If a string isn’t found in 'messages.po', gettext looks in the fallbacks ('ngne', 'click').
domain_translations.add_fallback(ngne_translations)
domain_translations.add_fallback(click_translations)

# Install gettext('_') into builtins for the chosen domain and localedir.
domain_translations.install()   # registers builtin _() and ngettext() globally.
