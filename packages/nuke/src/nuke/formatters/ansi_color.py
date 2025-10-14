import logging
from typing import Dict

from colorama import Fore, Style


# ----------------------------------------------------------------------------
# LOGGING FORMATTER
# ----------------------------------------------------------------------------


class AnsiColorFormatter(logging.Formatter):
    """
    ...
    """

    COLORS: Dict[int, str] = {
        logging.DEBUG: Fore.LIGHTCYAN_EX,
        logging.INFO: Fore.LIGHTBLUE_EX,
        logging.WARNING: Fore.LIGHTYELLOW_EX,
        logging.ERROR: Fore.LIGHTRED_EX,
        logging.CRITICAL: Fore.LIGHTMAGENTA_EX,
    }

    def format(self, record: logging.LogRecord):
        start_style: str = AnsiColorFormatter.COLORS.get(record.levelno, Style.RESET_ALL)
        end_style: str = Style.RESET_ALL

        return start_style + super().format(record).replace("[!]", Style.BRIGHT) + end_style
