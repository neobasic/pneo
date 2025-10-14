from typing import Final, Any, Dict

from colorama import Fore, Style

from nuke.settings.logging_levels import LogLevel


# ----------------------------------------------------------------------------
# ANSI COLORED PRINTS, FOR EACH LOGGING LEVEL.
# ----------------------------------------------------------------------------

COLOR_MAP: Final[Dict] = {
    LogLevel.NOTSET: Fore.LIGHTWHITE_EX,
    LogLevel.TRACE: Fore.LIGHTWHITE_EX,
    LogLevel.DEBUG: Fore.LIGHTCYAN_EX,
    LogLevel.INFO: Fore.LIGHTBLUE_EX,
    LogLevel.WARN: Fore.LIGHTYELLOW_EX,
    LogLevel.ERROR: Fore.LIGHTRED_EX,
    LogLevel.FATAL: Fore.LIGHTMAGENTA_EX,
}


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


def _level_color(level: str) -> str:
    ansi_color: str = COLOR_MAP.get(level, Style.NORMAL)
    return ansi_color


def _print(level: str, message: str, *args: Any):
    msg: str = _msg_format(message)
    if args:  # non-empty tuple evaluates to True
        msg = msg % args

    print(_level_color(level) + msg)


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
