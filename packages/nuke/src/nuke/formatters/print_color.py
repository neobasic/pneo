from typing import Final, Any, Dict

from colorama import Fore, Style

from nuke.setup.logging_levels import LogLevel
from nuke.setup.settings import Settings

# ----------------------------------------------------------------------------
# ANSI COLORED PRINTS, FOR EACH LOGGING LEVEL.
# ----------------------------------------------------------------------------

ICON_MAP: Final[Dict[LogLevel, str]] = {
    LogLevel.WARN: "⚠️ ",
    LogLevel.ERROR: "🛑 ",
    LogLevel.FATAL: "🚨 ",
}

COLOR_MAP: Final[Dict[LogLevel, str]] = {
    LogLevel.NOTSET: Fore.LIGHTWHITE_EX,
    LogLevel.TRACE: Fore.LIGHTGREEN_EX,
    LogLevel.DEBUG: Fore.LIGHTCYAN_EX,
    LogLevel.INFO: Fore.LIGHTBLUE_EX,
    LogLevel.WARN: Fore.LIGHTYELLOW_EX,
    LogLevel.ERROR: Fore.LIGHTRED_EX,
    LogLevel.FATAL: Fore.LIGHTMAGENTA_EX,
}


def is_enabled_for(level: LogLevel) -> bool:
    """
    Is this printer enabled for level 'level'?
    """

    # check if option -v or --verbose was used in command line.
    verbose: bool = Settings.get_instance().ctx.obj.get("verbose", False)
    if verbose:
        # anything is allowed to print when verbose is set.
        return True

    elif level in [LogLevel.DEBUG, LogLevel.TRACE]:
        return False

    else:
        return True


def _msg_format(message: str) -> str:
    if message and len(message) > 0:
        return (
            message.replace("\\*", "*")
            .replace("\\>", ">")
            .replace("\\<", "<")
            .replace("<*", Style.BRIGHT)
            .replace("*>", Style.NORMAL)
        )
    else:
        return message


def _level_icon(level: LogLevel) -> str:
    emoji_icon: str = ICON_MAP.get(level, "")
    return emoji_icon


def _level_color(level: LogLevel) -> str:
    # check if option -c or --color was used in command line.
    color: str = Settings.get_instance().ctx.obj.get("color", "auto")
    match color:
        case "auto":
            return COLOR_MAP.get(level, Style.NORMAL)
        case "black":
            return Fore.BLACK
        case "blue":
            return Fore.BLUE
        case "cyan":
            return Fore.CYAN
        case "green":
            return Fore.GREEN
        case "magenta":
            return Fore.MAGENTA
        case "red":
            return Fore.RED
        case "white":
            return Fore.WHITE
        case "yellow":
            return Fore.YELLOW

        # default color for output, if none is specified.
        case _:  # choice 'never'
            return Style.NORMAL


def _print(level: LogLevel, message: str, *args: Any):
    # check if the level has the severity necessary to print.
    if is_enabled_for(level):
        msg: str = _msg_format(message)
        if args:  # non-empty tuple evaluates to True
            msg = msg % args

        print(_level_color(level) + _level_icon(level) + msg)


def echo(message: str, *args: Any):
    _print(LogLevel.NOTSET, message, *args)


def p_trace(message: str, *args: Any):
    _print(LogLevel.TRACE, message, *args)


def p_debug(message: str, *args: Any):
    _print(LogLevel.DEBUG, message, *args)


def p_info(message: str, *args: Any):
    _print(LogLevel.INFO, message, *args)


def p_warn(message: str, *args: Any):
    _print(LogLevel.WARN, message, *args)


def p_error(message: str, *args: Any):
    _print(LogLevel.ERROR, message, *args)


def p_fatal(message: str, *args: Any):
    _print(LogLevel.FATAL, message, *args)
