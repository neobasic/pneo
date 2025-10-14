import os
import logging
import logging.config
import gettext
import locale
from typing import Dict, List, Final, Any, Optional

from nuke import AnsiColorFormatter, AppConfig, YamlConfigLoader, p_warn


# ----------------------------------------------------------------------------
# APPLICATION SETTINGS AND CONFIGURATION PATHS
# ----------------------------------------------------------------------------

APP_NAME: str = "pneo"
APP_ROOT_PACKAGE: str = APP_NAME
APP_CONFIG_PACKAGE: str = APP_ROOT_PACKAGE + ".config"


# ----------------------------------------------------------------------------
# SETTINGS PRIVATE HELPERS
# ----------------------------------------------------------------------------


def _setup_logging(config: AppConfig):
    log_level: str = config.log_config.level
    log_level = log_level.casefold() if log_level else "notset"

    log_config_file: str = ""
    match log_level:
        case "info" | "warning" | "error" | "critical":
            # this logging configuration has file:
            log_config_file = "info.yaml"

        case "debug":
            # this logging configuration has file:
            log_config_file = "debug.yaml"

        case _:  # "notset"
            # this logging configuration uses console, does not have file:
            log_config_file = "notset.yaml"

    # load the logging configuration from inside the app packages (resource).
    loader: YamlConfigLoader = YamlConfigLoader()
    log_config_dict: Dict[str, Dict[str, Any]] = loader.load_config_resource(
        config.id.app_anchor_config, log_config_file
    )

    if log_config_file != "notset.yaml":
        log_filename: str = str(config.id.app_log_path)  # default value
        if config.log_config.filename and config.log_config.filename.lower() != "none":
            # just in case there is '~' in file path.
            log_filename = os.path.expanduser(config.log_config.filename)

        # Ensure log path directory exists in current OS.
        log_dir: str = os.path.dirname(log_filename)
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)

        log_config_dict["handlers"]["logfile"]["level"] = log_level.upper()
        log_config_dict["handlers"]["logfile"]["filename"] = log_filename

    # as soon as the app is loaded, set the logging configuration:
    logging.config.dictConfig(config=log_config_dict)

    # customize the console formatter to show colors on terminal:
    console_handler: Optional[logging.Handler] = logging.getHandlerByName("console")
    if console_handler:
        fmt: str = log_config_dict["formatters"]["simple"]["format"]
        datefmt: str = "%H:%M:%S"  # don't need to show the full date/day every moment.
        console_formatter: logging.Formatter = AnsiColorFormatter(fmt=fmt, datefmt=datefmt)
        console_handler.setFormatter(console_formatter)


def _setup_internationalization(config: AppConfig):
    msg_domain: Final[str] = "messages"
    valid_locales: List[str] = ["pt_BR", "en_US"]
    default_locale: str = "en_US"  # fallback language.

    # check the configured locale language:
    lang: Optional[str] = config.i18n_config.locale
    if lang not in valid_locales:
        # get the default locale already configured of OS.
        try:
            # Try to set the locale from the environment
            locale.setlocale(locale.LC_ALL, "")
            lang, _ = locale.getlocale()
        except locale.Error:
            lang = default_locale  # Could not determine locale from environment

        if lang not in valid_locales:
            lang = default_locale

    # configure the choosen locale as global locale:
    value_locale: str = lang + ".UTF-8"
    try:
        locale.setlocale(locale.LC_ALL, value_locale)
    except locale.Error:
        p_warn("Locale '%s' not supported. Falling back to system default.", value_locale)
        # Fallback to system default if specific UTF-8 is not available
        locale.setlocale(locale.LC_ALL, "")

    # include the default-locale at the end, as a fallback.
    languages: List = [lang]
    if default_locale not in languages:
        languages.append(default_locale)

    # path to the locale folder (defaults to src/app/locale, or relative to this file)
    heredir: str = os.path.abspath(os.path.dirname(__file__))
    localedir: str = os.path.normpath(os.path.join(heredir, "locale"))

    # fallback=True avoids exceptions if any file .mo is missing.
    global_translations: gettext.NullTranslations = gettext.translation(
        domain=msg_domain, localedir=localedir, languages=languages, fallback=True
    )

    # Install gettext and ngettext into builtins for the chosen domain and localedir.
    global_translations.install({"gettext", "ngettext"})

    # force the localization methods in nuke, easier to configure .pyi typing files.
    import nuke
    import builtins

    nuke.__dict__["gettext"] = builtins.__dict__["gettext"]
    nuke.__dict__["ngettext"] = builtins.__dict__["ngettext"]

    # HACKING PATCH: Because `.install()` does not update gettext and ngettext,
    # the import `from gettext import gettext as _, ngettext` does not reflect
    # the methods `gettext, ngettext` from the domain translation class.

    # These are still good practice for compatibility with libraries that might use them.
    gettext.bindtextdomain(msg_domain, localedir)
    # legacy implementation of gettext still check envars: LANGUAGE, LC_ALL, LC_MESSAGES, LANG
    os.environ["LANGUAGE"] = ":".join(languages)


# ----------------------------------------------------------------------------
# APPLICATION INITIALIZATION
# ----------------------------------------------------------------------------

# Initializes the application by loading configuration, setting up logging,
# and configuring internationalization. This should be called once at startup (import).

# 1. Load configuration
app_config: AppConfig = AppConfig.init_instance(APP_NAME, APP_ROOT_PACKAGE, APP_CONFIG_PACKAGE)

# 2. Setup logging (do this first to log subsequent steps)
_setup_logging(app_config)
log: logging.Logger = logging.getLogger(__name__)
log.debug("Logging configured.")

# 3. Setup i18n
_setup_internationalization(app_config)
log.debug("Internationalization configured.")

# 4. Initial setup ok
log.debug("Application initialized successfully.")
