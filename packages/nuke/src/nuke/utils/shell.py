"""Shell routines for NT or Posix depending on what system we're on."""

import os
from pathlib import Path
from typing import Optional


# ----------------------------------------------------------------------------
# FILESYSTEM ROUTINES
# ----------------------------------------------------------------------------


def make_accessible_dir(dir: Optional[str]) -> bool:
    """
    Check if a directory is accessible: exists and user can write onto it.
    """

    # just to be sure.
    if not dir:
        return False

    # if the path does not exist, try to create it.
    dirpath: Path = Path(dir)
    if not dirpath.exists():
        try:
            os.makedirs(dirpath, exist_ok=True)
        except PermissionError:
            # If do not have permission to create the directory: not accessible.
            return False

    # Now that path exists, check if can write onto it.
    return os.access(dirpath, os.W_OK)
