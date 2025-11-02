import gettext
import locale
import logging
import logging.config
import os

import nuke


# ----------------------------------------------------------------------------
# SETTINGS PRIVATE HELPERS
# ----------------------------------------------------------------------------

def _setup_logging(settings: nuke.Settings):
    from typing import Any

    log_level: str = settings.log.level
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
    loader: nuke.YamlConfigLoader = nuke.YamlConfigLoader()
    log_config_dict: dict[str, dict[str, Any]] = loader.load_config_resource(
        settings.app.anchor_config, log_config_file
    )

    if log_config_file != "notset.yaml":
        log_filename: str = str(settings.app.log_path)  # default value
        if settings.log.filename and settings.log.filename.lower() != "none":
            # just in case there is '~' in file path.
            log_filename = os.path.expanduser(settings.log.filename)

        # Ensure log path directory exists in current OS.
        log_dir: str = os.path.dirname(log_filename)
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)

        log_config_dict["handlers"]["logfile"]["level"] = log_level.upper()
        log_config_dict["handlers"]["logfile"]["filename"] = log_filename

    # as soon as the app is loaded, set the logging configuration:
    logging.config.dictConfig(config=log_config_dict)

    # customize the console formatter to show colors on terminal:
    console_handler: logging.Handler | None = logging.getHandlerByName("console")
    if console_handler:
        fmt: str = log_config_dict["formatters"]["simple"]["format"]
        datefmt: str = "%H:%M:%S"  # don't need to show the full date/day every moment.
        console_formatter: logging.Formatter = nuke.AnsiColorFormatter(fmt=fmt, datefmt=datefmt)
        console_handler.setFormatter(console_formatter)


def _setup_internationalization(settings: nuke.Settings):
    msg_domain: str = "messages"
    valid_locales: list[str] = ["pt_BR", "en_US"]
    default_locale: str = "en_US"  # fallback language.

    # check the configured locale language:
    lang: str | None = settings.i18n.locale
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

    # configure the chosen locale as global locale:
    value_locale: str = lang + ".UTF-8"
    try:
        locale.setlocale(locale.LC_ALL, value_locale)
    except locale.Error:
        nuke.p_warn("Locale '%s' not supported. Falling back to system default.", value_locale)
        # Fallback to system default if specific UTF-8 is not available
        locale.setlocale(locale.LC_ALL, "")

    # include the default-locale at the end, as a fallback.
    languages: list = [lang]
    if default_locale not in languages:
        languages.append(default_locale)

    # path to the locale folder (defaults to src/app/locale, or relative to this file)
    heredir: str = os.path.abspath(os.path.dirname(__file__))
    localedir: str = os.path.normpath(os.path.join(heredir, "locale"))

    # fallback=True avoids exceptions if some file .mo is missing.
    global_translations: gettext.NullTranslations = gettext.translation(
        domain=msg_domain, localedir=localedir, languages=languages, fallback=True
    )

    # Install gettext and ngettext into builtins for the chosen domain and localedir.
    global_translations.install({"gettext", "ngettext"})

    # force the localization methods in nuke, easier import and to configure .pyi typing files.
    nuke.gettext = global_translations.gettext
    nuke.ngettext = global_translations.ngettext

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
_settings: nuke.Settings = nuke.Settings.init_instance(
    name="pneo",
    anchor_root="pneo",
    anchor_config="pneo.config",
    config_ext="conf"
)

# 2. Setup logging (do this first to log subsequent steps)
_setup_logging(_settings)
# logging.debug("Logging configured.")

# 3. Setup i18n
_setup_internationalization(_settings)
# logging.debug("Internationalization configured.")

# 4. Initial setup ok
# logging.debug("Application initialized successfully.")
