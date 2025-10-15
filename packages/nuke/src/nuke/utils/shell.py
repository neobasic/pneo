"""Shell routines for NT or Posix depending on what system we're on."""

import logging
import os
from os import PathLike
from typing import AnyStr


# ----------------------------------------------------------------------------
# FILESYSTEM ROUTINES
# ----------------------------------------------------------------------------

def check_readable_dir(dir_name: str | PathLike[AnyStr] | None) -> bool:
    """
    Check if the given directory is non-empty, valid, exists, and is readable.

    Args:
        dir_name: A filesystem path (str, bytes, or PathLike).

    Returns:
        True if the path is valid, exists, and is readable by the user; False otherwise.
    """

    # just to be sure.
    if not dir_name:
        # Handles None, empty string, or similar falsy values
        return False

    # Convert PathLike (could be str, bytes, or pathlib.Path) to filesystem path
    dir_path = os.fspath(dir_name)
    dir_exists: bool = os.path.exists(dir_path)

    # Check if dir_path exists
    if not dir_exists:
        return False

    # Optionally check if it’s a directory.
    if not os.path.isdir(dir_path):
        return False

    # Check if user has read access
    if not os.access(dir_path, os.R_OK):
        return False

    # given path is non-empty, valid, exists, and is readable.
    return True


def check_writable_dir(dir_name: str | PathLike[AnyStr] | None) -> bool:
    """
    Check if the given directory is non-empty, valid, exists, and is readable and writable.

    Args:
        dir_name: A filesystem path (str, bytes, or PathLike).

    Returns:
        True if the path is valid, exists, is readable and writable by the user; False otherwise.
    """

    # just to be sure.
    if not dir_name:
        # Handles None, empty string, or similar falsy values
        return False

    # Convert PathLike (could be str, bytes, or pathlib.Path) to filesystem path
    dir_path = os.fspath(dir_name)
    dir_exists: bool = os.path.exists(dir_path)

    # Check if dir_path exists
    if not dir_exists:
        return False

    # Optionally check if it’s a directory.
    if not os.path.isdir(dir_path):
        return False

    # Check if user can read and write onto it.
    if not os.access(dir_path, os.R_OK | os.W_OK):
        return False

    # given path is non-empty, valid, exists, and is readable and writable.
    return True


def make_accessible_dir(dir_name: str | PathLike[AnyStr] | None) -> bool:
    """
    Check if a directory is accessible: dir_name must exist and user should be able to write onto it.
    """

    # just to be sure.
    if not dir_name:
        # Handles None, empty string, or similar falsy values
        return False

    # Convert PathLike (could be str, bytes, or pathlib.Path) to filesystem path
    dir_path = os.fspath(dir_name)
    dir_exists: bool = os.path.exists(dir_path)

    # Optionally check if it’s a directory.
    if dir_exists and not os.path.isdir(dir_path):
        return False

    # Check if dir_path exists...
    if not dir_exists:
        try:
            # ...and if not, create it.
            os.makedirs(dir_path, exist_ok=True)
        except Exception as e:  # catches PermissionError
            logging.error("Failed to create directory '%s': %r", dir_path, e)
            # If user do not have permission to create the directory, it is not accessible.
            return False

    # Now that path exists, check if user can read and write onto it.
    if not os.access(dir_path, os.R_OK | os.W_OK):
        return False

    # given path is non-empty, valid, exists, and is writable.
    return True
