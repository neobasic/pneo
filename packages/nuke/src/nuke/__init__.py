from gettext import gettext, ngettext

from nuke.utils.decorators import fdocstr
from nuke.settings.app_config import AppConfig
from nuke.settings.logging_levels import LogLevel
from nuke.settings.config_strategies import ConfigLoader, YamlConfigLoader
from nuke.formatters.ansi_color import AnsiColorFormatter
from nuke.formatters.print_color import (
    echo,
    p_trace,
    p_debug,
    p_info,
    p_warn,
    p_error,
    p_fatal,
)


# Application settings, color-formatter and helper functions are now globally available.
__all__ = [
    "gettext",
    "ngettext",
    "fdocstr",
    "AppConfig",
    "LogLevel",
    "ConfigLoader",
    "YamlConfigLoader",
    "AnsiColorFormatter",
    "echo",
    "p_trace",
    "p_debug",
    "p_info",
    "p_warn",
    "p_error",
    "p_fatal",
]
