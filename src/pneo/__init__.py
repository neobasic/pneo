import os
import yaml
import logging.config
import logging
import gettext
import locale
import builtins
from typing import Optional, Dict, List
from pathlib import Path
from importlib import resources
from enum import StrEnum, auto
from dataclasses import dataclass
from configparser import ConfigParser
from platformdirs import user_config_path, user_log_path


__all__ = [
    'USER_HOME_PATH', 'NEOBASIC_HOME_PATH', 'CONFIG_FILE_PATH', 'CONFIG_FILE', 'AppConfig', 'getAppConfig'
]


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
# APPLICATION SETTINGS AND CONFIGURATION PATHS
# ----------------------------------------------------------------------------

APP_NAME: str = "pneo"
APP_ROOT_PACKAGE: str = APP_NAME
APP_CONFIG_PACKAGE: str = APP_ROOT_PACKAGE + ".config"

CONFIG_FILE: str = APP_NAME + ".conf"
CONFIG_FILE_PATH: Path = user_config_path(appname=APP_NAME) / CONFIG_FILE

LOG_FILE: str = APP_NAME + ".log"
LOG_FILE_PATH: Path = user_log_path(appname=APP_NAME) / LOG_FILE

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

# first, just declare as singleton instance, then get the application settings on start (main).
app_config: AppConfig = None


# ----------------------------------------------------------------------------
# SETUP PUBLIC API
# ----------------------------------------------------------------------------

# Read the content of a configuration file inside the project, from a module.
def read_config_resource(filename: str) -> str:
    content: str = None
    with resources.open_text(APP_CONFIG_PACKAGE, filename) as f:
        content = f.read()

    return content


def getAppConfig(config_path: Path = CONFIG_FILE_PATH) -> AppConfig:
    global app_config
    
    # check like it is a singleton
    if app_config is None:
        # first time: load the configuration now
        config_parser = _read_config_file(config_path)

        # load the settings in the global config instance:
        i18n_config = I18nConfig(**config_parser["i18n"])
        theme_config = ThemeConfig(**config_parser["theme"])
        log_config = LoggingConfig(**config_parser["logging"])
        app_config = AppConfig(i18nConfig = i18n_config, themeConfig = theme_config, logConfig = log_config)
    
    return app_config


# ----------------------------------------------------------------------------
# SETTINGS PRIVATE HELPERS
# ----------------------------------------------------------------------------

# Read the content of a configuration file outside, from a OS path.
def _read_config_file(file_path: Path | None) -> ConfigParser:
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
    default_settings: str = read_config_resource(CONFIG_FILE)
    # Read the settings inside the project (default configuration).
    config_parser.read_string(default_settings)

    return config_parser


def _setup_logging(config: AppConfig):
    log_level: str = config.logConfig.level
    log_level = log_level.casefold() if log_level is not None else "notset"

    log_config_file: str
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
        log_filename: str = str(LOG_FILE_PATH)  # default value
        if config.logConfig.filename and config.logConfig.filename.lower() != "none":
            # just in case there is '~' in file path.
            log_filename = os.path.expanduser(config.logConfig.filename)
        
        # Ensure log path directory exists in current OS.
        log_dir: str = os.path.dirname(log_filename)
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)

        log_config_dict["handlers"]["logfile"]["level"] = log_level.upper()
        log_config_dict["handlers"]["logfile"]["filename"] = log_filename

    # as soon as the app is loaded, set the logging configuration:
    logging.config.dictConfig(config=log_config_dict)


def _setup_internationalization(config: AppConfig):
    MSG_DOMAIN: str = "messages"
    VALID_LOCALES: List[str] = ['pt_BR', 'en_US']
    DEFAULT_LOCALE: str = 'en_US'  # fallback language.

    # check the configured locale language:
    lang: str = config.i18nConfig.locale
    if lang not in VALID_LOCALES:
        # get the default locale already configured of OS.
        try:
            # Try to set the locale from the environment
            locale.setlocale(locale.LC_ALL, '')
            lang, encod = locale.getlocale()
        except locale.Error:
            lang = DEFAULT_LOCALE  # Could not determine locale from environment
        
        if lang not in VALID_LOCALES:
            lang = DEFAULT_LOCALE

    # configure the choosen locale as global locale:
    try:
        value_locale: str = lang + ".UTF-8"
        locale.setlocale(locale.LC_ALL, value_locale)
    except locale.Error:
        logging.getLogger(__name__).warning(f"Locale '{value_locale}' not supported. Falling back to system default.")
        locale.setlocale(locale.LC_ALL, '')  # Fallback to system default if specific UTF-8 is not available

    # include the default-locale at the end, as a fallback.
    languages: List = [lang]
    if DEFAULT_LOCALE not in languages:
        languages.append(DEFAULT_LOCALE)

    # path to the locale folder (defaults to src/app/locale, or relative to this file)
    heredir: str = os.path.abspath(os.path.dirname(__file__))
    localedir: str = os.path.normpath(os.path.join(heredir, "locale"))

    # fallback=True avoids exceptions if any file .mo is missing.
    global_translations = gettext.translation(domain=MSG_DOMAIN, localedir=localedir, languages=languages, fallback=True)

    # Install gettext and ngettext into builtins for the chosen domain and localedir.
    global_translations.install({'gettext', 'ngettext'})

    # HACKING PATCH: Because `.install()` does not update gettext and ngettext,
    # the import `from gettext import gettext as _, ngettext` does not reflect
    # the methods `gettext, ngettext` from the domain translation class.

    # These are still good practice for compatibility with libraries that might use them.
    gettext.bindtextdomain(MSG_DOMAIN, localedir)
    # legacy implementation of gettext still check envars: LANGUAGE, LC_ALL, LC_MESSAGES, LANG
    os.environ["LANGUAGE"] = ':'.join(languages)


# decorator to patch the docstring of a function, to enable
# the use of gettext '_' in a docstring before the click library.
def _fdocstr(docstr: str):
    def wrapper(func):
        func.__doc__ = docstr
        return func
    return wrapper


# ----------------------------------------------------------------------------
# APPLICATION INITIALIZATION
# ----------------------------------------------------------------------------

# Initializes the application by loading configuration, setting up logging,
# and configuring internationalization. This should be called once at startup (import).

# 1. Load configuration
app_config = getAppConfig()

# 2. Setup logging (do this first to log subsequent steps)
_setup_logging(app_config)
log = logging.getLogger(__name__)
log.debug("Logging configured.")

# 3. Setup i18n
_setup_internationalization(app_config)
log.debug("Internationalization configured.")

# 4. Initial setup ok
log.debug("Application initialized successfully.")

# put the docstring decorator in the global scope for all modules.
builtins.__dict__['fdocstr'] = _fdocstr

