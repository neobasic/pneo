import logging
import os
from pathlib import Path

import click
from nuke import gettext as _, Settings, fdocstr
from nuke.formatters.print_color import p_error
from pneo.command.receiver.receiver_version import show_project_version, set_project_version

# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()

# ----------------------------------------------------------------------------
# CLICK: COMMAND VERSION
# ----------------------------------------------------------------------------

_version_short_help: str = _("Read or update the current project's version, or some other project manifest file.")


@click.command(options_metavar=_("<OPTIONS>"), short_help=_version_short_help)
@click.option(
    "--path",
    "-p",
    required=False,
    type=click.Path(exists=True, file_okay=True, dir_okay=True),
    help=_("Path to the project manifest file."),
)
@click.option(
    "--frozen",
    "-f",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Update the version without re-locking the project."),
)
@click.option(
    "--bump",
    "-b",
    required=False,
    type=click.Choice(
        ["major", "minor", "patch", "stable", "alpha", "beta", "rc", "post", "dev"],
        case_sensitive=False,
    ),
    help=_("Increment the project version using the given semantics."),
)
@click.argument(
    "new-version",
    required=False,
    type=click.STRING,
    metavar=_("<NEW-VERSION>"),
)
@click.pass_context
@fdocstr(_version_short_help)
def version(context: click.Context, path: Path, frozen: bool, bump: str, new_version: str) -> None:
    logger.debug("Entering: path=%s, frozen=%s, bump=%s, version=%s", path, frozen, next, version)

    # Check if the given path has a manifest file.
    manifest_file: str = "manifest.toml"
    if path:
        manifest_file = os.path.join(path, "manifest.toml")
        if not os.path.exists(manifest_file):
            p_error(_("Error: There is no manifest file in '%s'."), path)
            exit(1)

    elif not os.path.exists(manifest_file):
        p_error(_("Error: There is no manifest file in current directory."))
        exit(1)

    # Check if just want to see the version...
    if not frozen and not bump and not new_version:
        # proceed with the displaying of the current version.
        show_project_version(manifest_file)

    else:
        set_project_version(manifest_file, new_version, bump, frozen)
