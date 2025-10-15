import logging
from pathlib import Path

import click
from nuke import gettext as _, Settings, fdocstr

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
    "--next",
    "-n",
    required=False,
    type=click.Choice(
        ["major", "minor", "patch", "stable", "alpha", "beta", "rc", "post", "dev"],
        case_sensitive=False,
    ),
    help=_("Increment the project version using the given semantics."),
)
@click.argument(
    "version",
    required=False,
    type=click.STRING,
    metavar=_("<VERSION>"),
)
@click.pass_context
@fdocstr(_version_short_help)
def version(context: click.Context, path: Path, frozen: bool, next: bool, version: str) -> None:
    logger.debug("Entering: path=%s, frozen=%s, next=%s, version=%s", path, frozen, next, version)

    pass
