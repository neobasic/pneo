def is_quoted(s: str | None) -> bool:
    """
    Check if a string is quoted with matching double quotes, single quotes, or backticks.

    A string is considered quoted if it starts and ends with the same character,
    and that character is one of: `"`, `'`, or `` ` ``.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is quoted, False otherwise.
    """

    if not s or len(s) < 2:
        return False

    return s[0] == s[-1] and s[0] in ('"', "'", '`')


def strip_quotes(s: str | None) -> str | None:
    """
    Strip surrounding double quotes, single quotes or backticks from a string.

    If the string is None or does not start with a double quote, single quotes or backticks,
    the original string is returned unchanged.
    """

    if s is None or not is_quoted(s):
        return s

    return s[1:-1]
