from enum import StrEnum, auto


# ----------------------------------------------------------------------------
# LOGGING LEVELS TO SETUP LOGGING AND PRINT WITH ANSI COLORS
# ----------------------------------------------------------------------------


class LogLevel(StrEnum):
    """
    ...
    """

    NOTSET = auto()
    TRACE = auto()
    DEBUG = auto()
    INFO = auto()
    WARN = auto()
    ERROR = auto()
    FATAL = auto()
