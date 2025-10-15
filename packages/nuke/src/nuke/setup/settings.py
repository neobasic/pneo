import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import ClassVar, Dict, Final, Optional, Any

from platformdirs import user_config_path, user_log_path

import click
from nuke.setup.config_strategies import get_strategy, ConfigLoader
from nuke.utils.shell import make_accessible_dir

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
class AppIdentity:
    """..."""

    # application identification.
    name: str
    anchor_root: str
    anchor_config: str
    default_config: str

    # Directories used to store the app setup and logging.
    config_path: Path
    config_file: str
    log_path: Path
    log_file: str

    user_home_path: Path
    neobasic_home_path: Path

    def __init__(
            self,
            name: str,
            anchor_root: Optional[str] = None,
            anchor_config: Optional[str] = None,
    ):
        self.name = name
        self.default_config = ""  # force first time reading in init-instance.

        if anchor_root:
            self.anchor_root = anchor_root
        else:
            self.anchor_root = name

        if anchor_config:
            self.anchor_config = anchor_config
        else:
            self.anchor_config = APP_CONFIG_ANCHOR % self.anchor_root

        # what can infer based on app name:
        self.config_file = APP_CONFIG_FILE % name
        self.log_file = APP_LOG_FILE % name

        # what must check, but also based on app name:
        self.user_home_path = Path.home()

        # check if user declared an environment variable `NEOBASIC_HOME`.
        envar_neobasic_home: str = os.getenv(ENVAR_NEOBASIC_HOME)
        if envar_neobasic_home and make_accessible_dir(envar_neobasic_home):
            # if user declared an env var of valid dir, use it for all paths.
            self.neobasic_home_path = Path(envar_neobasic_home)
            self.config_path = self.neobasic_home_path / self.config_file
            self.log_path = self.neobasic_home_path / DIR_NEOBASIC_LOGS / self.log_file

        else:
            # use the default path for neobasic-home.
            self.neobasic_home_path = self.user_home_path / DIR_NEOBASIC_HOME

            # if there is no (valid) env var, but there is the app name, use it.
            if self.name:
                self.config_path = (user_config_path(appname=self.name) / self.config_file)
                self.log_path = user_log_path(appname=self.name) / self.log_file

            else:
                # if there is no env var and no app name, use the default path.
                self.config_path = self.neobasic_home_path / self.config_file
                self.log_path = self.neobasic_home_path / DIR_NEOBASIC_LOGS / self.log_file


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
class Settings:
    """..."""

    # class-level attributes and methods
    _instance: ClassVar["Settings"]

    @classmethod
    def init_instance(
            cls,
            name: str,
            anchor_root: Optional[str] = None,
            anchor_config: Optional[str] = None,
            config_ext: Optional[str] = None,
    ) -> "Settings":
        # identify the app:
        app_identity: AppIdentity = AppIdentity(name, anchor_root, anchor_config)

        # load the default configuration inside the package, just in case...
        loader: ConfigLoader = get_strategy(config_ext)
        app_identity.default_config = loader.load_content_resource(app_identity.anchor_config, app_identity.config_file)

        # check if there is a config file in neobasic-home, defined by an envar.
        config_dict: Dict[str, Dict[str, Any]] = loader.load_config_file(app_identity.config_path)

        # if there is no file, or if it is empty of invalid...
        if not config_dict:
            # ... parse the default config inside the config package (anchor) of the app.
            config_dict = loader.load_config_str(app_identity.default_config)

        # load the setup in the global config instance:
        i18n_config: I18nConfig = I18nConfig(**config_dict["i18n"])
        theme_config: ThemeConfig = ThemeConfig(**config_dict["theme"])
        log_config: LoggingConfig = LoggingConfig(**config_dict["logging"])
        cls._instance = Settings(
            app=app_identity,
            i18n=i18n_config,
            theme=theme_config,
            log=log_config,
        )
        return cls._instance

    @classmethod
    def get_instance(cls) -> "Settings":
        # check like it is a singleton.
        if cls._instance is None:
            # first time: load the configuration now
            cls.init_instance("pneo")

        return cls._instance

    # instance attributes and methods (object-level)
    app: AppIdentity
    i18n: I18nConfig
    theme: ThemeConfig
    log: LoggingConfig
    ctx: click.core.Context = field(init=False)  # not passed to __init__

    def to_dict(self) -> Dict[str, Dict[str, str]]:
        dict_config: Dict[str, Dict[str, str]] = {
            "app": {
                "name": self.app.name,
                "anchor_root": self.app.anchor_root,
                "anchor_config": self.app.anchor_config,
                "config_path": str(self.app.config_path),
                "config_file": self.app.config_file,
                "log_path": str(self.app.log_path),
                "log_file": self.app.log_file,
                "user_home_path": str(self.app.user_home_path),
                "neobasic_home_path": str(self.app.neobasic_home_path),
            },
            "i18n": {
                "locale": self.i18n.locale,
                "timezone": self.i18n.timezone,
                "date_format": self.i18n.date_format.replace("%", "%%"),
                "time_format": self.i18n.time_format.replace("%", "%%"),
                "decimal_separator": self.i18n.decimal_separator,
                "thousands_separator": self.i18n.thousands_separator,
                "direction": self.i18n.direction,
            },
            "theme": {
                "title_color": self.theme.title_color,
                "section_color": self.theme.section_color,
                "key_color": self.theme.key_color,
                "value_color": self.theme.value_color,
                "debug_color": self.theme.debug_color,
                "info_color": self.theme.info_color,
                "warning_color": self.theme.warning_color,
                "error_color": self.theme.error_color,
                "critical_color": self.theme.critical_color,
                "success_color": self.theme.success_color,
            },
            "logging": {
                "level": self.log.level,
                "filename": self.log.filename,
            },
        }

        return dict_config
