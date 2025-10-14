import os
from pathlib import Path
from dataclasses import dataclass
from typing import ClassVar, Dict, Final, Optional, Any

from platformdirs import user_config_path, user_log_path

from nuke.utils.shell import make_accessible_dir
from nuke.settings.config_strategies import get_strategy, ConfigLoader


# ----------------------------------------------------------------------------
# NEOBASIC DEFAULT SETTINGS FOR ALL TOOLS OF ECOSYSTEM
# ----------------------------------------------------------------------------

ENVAR_NEOBASIC_HOME: Final[str] = "NEOBASIC_HOME"

DIR_NEOBASIC_HOME: Final[str] = ".neobasic"
DIR_NEOBASIC_LOGS: Final[str] = "logs"

APP_CONFIG_ANCHOR: Final[str] = "%s.config"
APP_CONFIG_FILE: Final[str] = "%s.conf"
APP_LOG_FILE: Final[str] = "%s.log"


# ----------------------------------------------------------------------------
# APPLICATION CONFIGURATION MODEL
# ----------------------------------------------------------------------------


@dataclass
class Identity:
    """..."""

    # application identification.
    app_name: str
    app_anchor_root: str
    app_anchor_config: str
    app_default_config: str

    # Directories used to store the app settings and logging.
    app_config_path: Path
    app_config_file: str
    app_log_path: Path
    app_log_file: str

    user_home_path: Path
    neobasic_home_path: Path

    def __init__(
        self,
        name: str,
        anchor_root: Optional[str] = None,
        anchor_config: Optional[str] = None,
    ):
        self.app_name = name
        self.app_default_config = ""  # force first time reading in init-instance.

        if anchor_root:
            self.app_anchor_root = anchor_root
        else:
            self.app_anchor_root = name

        if anchor_config:
            self.app_anchor_config = anchor_config
        else:
            self.app_anchor_config = APP_CONFIG_ANCHOR % self.app_anchor_root

        # what can infer based on app name:
        self.app_config_file = APP_CONFIG_FILE % name
        self.app_log_file = APP_LOG_FILE % name

        # what have to check, but also based on app name:
        self.user_home_path = Path.home()

        # check if user declared an environment variable `NEOBASIC_HOME`.
        envar_neobasic_home: Optional[str] = os.getenv(ENVAR_NEOBASIC_HOME)
        if envar_neobasic_home and make_accessible_dir(envar_neobasic_home):
            # if user declared an env var of valid dir, use it for all paths.
            self.neobasic_home_path = Path(envar_neobasic_home)
            self.app_config_path = self.neobasic_home_path / self.app_config_file
            self.app_log_path = self.neobasic_home_path / DIR_NEOBASIC_LOGS / self.app_log_file

        else:
            # use the default path for neobasic-home.
            self.neobasic_home_path = self.user_home_path / DIR_NEOBASIC_HOME

            # if there is no (valid) env var, but there is the app name, use it.
            if self.app_name:
                self.app_config_path = (
                    user_config_path(appname=self.app_name) / self.app_config_file
                )
                self.app_log_path = user_log_path(appname=self.app_name) / self.app_log_file

            else:
                # if there is no env var and no app name, use the default path.
                self.app_config_path = self.neobasic_home_path / self.app_config_file
                self.app_log_path = self.neobasic_home_path / DIR_NEOBASIC_LOGS / self.app_log_file


@dataclass
class I18nConfig:
    """..."""

    locale: str
    timezone: str
    date_format: str
    time_format: str
    decimal_separator: str
    thousands_separator: str
    direction: str


@dataclass
class ThemeConfig:
    """..."""

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
    """..."""

    level: str
    filename: str


@dataclass
class AppConfig:
    """..."""

    # class-level attributes and methods
    _instance: ClassVar["AppConfig"]

    @classmethod
    def init_instance(
        cls,
        name: str,
        anchor_root: Optional[str] = None,
        anchor_config: Optional[str] = None,
        config_ext: Optional[str] = None,
    ) -> "AppConfig":
        # identify the app:
        id: Identity = Identity(name, anchor_root, anchor_config)

        # load the default configuration inside the package, just in case...
        loader: ConfigLoader = get_strategy(config_ext)
        id.app_default_config = loader.load_content_resource(
            id.app_anchor_config, id.app_config_file
        )

        # check if there is a config file in neobasic-home, defined by an envar.
        config_dict: Dict[str, Dict[str, Any]] = loader.load_config_file(id.app_config_path)

        # if there is no file, or if it is empty of invalid...
        if not config_dict:
            # ... parse the default config inside the config package (anchor) of the app.
            config_dict = loader.load_config_str(id.app_default_config)

        # load the settings in the global config instance:
        i18n_config: I18nConfig = I18nConfig(**config_dict["i18n"])
        theme_config: ThemeConfig = ThemeConfig(**config_dict["theme"])
        log_config: LoggingConfig = LoggingConfig(**config_dict["logging"])
        cls._instance = AppConfig(
            id=id,
            i18n_config=i18n_config,
            theme_config=theme_config,
            log_config=log_config,
        )
        return cls._instance

    @classmethod
    def get_instance(cls) -> "AppConfig":
        # check like it is a singleton.
        if cls._instance is None:
            # first time: load the configuration now
            cls.init_instance("pneo")

        return cls._instance

    # instance attributes and methods (object-level)
    id: Identity
    i18n_config: I18nConfig
    theme_config: ThemeConfig
    log_config: LoggingConfig

    def to_dict(self) -> Dict[str, Dict[str, str]]:
        dict_config: Dict[str, Dict[str, str]] = {
            "app": {
                "app_name": self.id.app_name,
                "app_anchor_root": self.id.app_anchor_root,
                "app_anchor_config": self.id.app_anchor_config,
                "app_config_path": str(self.id.app_config_path),
                "app_config_file": self.id.app_config_file,
                "app_log_path": str(self.id.app_log_path),
                "app_log_file": self.id.app_log_file,
                "user_home_path": str(self.id.user_home_path),
                "neobasic_home_path": str(self.id.neobasic_home_path),
            },
            "i18n": {
                "locale": self.i18n_config.locale,
                "timezone": self.i18n_config.timezone,
                "date_format": self.i18n_config.date_format.replace("%", "%%"),
                "time_format": self.i18n_config.time_format.replace("%", "%%"),
                "decimal_separator": self.i18n_config.decimal_separator,
                "thousands_separator": self.i18n_config.thousands_separator,
                "direction": self.i18n_config.direction,
            },
            "theme": {
                "title_color": self.theme_config.title_color,
                "section_color": self.theme_config.section_color,
                "key_color": self.theme_config.key_color,
                "value_color": self.theme_config.value_color,
                "debug_color": self.theme_config.debug_color,
                "info_color": self.theme_config.info_color,
                "warning_color": self.theme_config.warning_color,
                "error_color": self.theme_config.error_color,
                "critical_color": self.theme_config.critical_color,
                "success_color": self.theme_config.success_color,
            },
            "logging": {
                "level": self.log_config.level,
                "filename": self.log_config.filename,
            },
        }

        return dict_config
