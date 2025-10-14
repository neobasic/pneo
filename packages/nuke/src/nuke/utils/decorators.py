from typing import Callable, TypeVar


# ----------------------------------------------------------------------------
# DOCSTRING SETTER
# ----------------------------------------------------------------------------

F = TypeVar("F", bound=Callable[..., object])


def fdocstr(docstr: str) -> Callable[[F], F]:
    """
    Decorator to patch the docstring of a function, to enable
    the use of gettext '_' in a docstring before the click library.
    """

    def wrapper(func: F) -> F:
        func.__doc__ = docstr
        return func

    return wrapper
