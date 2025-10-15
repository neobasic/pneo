import logging
from pathlib import Path

import click
from nuke import gettext as _, Settings, fdocstr, p_error
from nuke.utils.shell import check_writable_dir
from pneo.command.receiver.receiver_clean import clean_project_path, clean_project

# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()

# ----------------------------------------------------------------------------
# CLICK: COMMAND CLEAN
# ----------------------------------------------------------------------------

_clean_short_help: str = _(
    "Remove artifacts of project that pneo has generated in the past, in an existing <PATH> directory. [default: .]")


@click.command(options_metavar=_("<OPTIONS>"), short_help=_clean_short_help)
@click.option(
    "--keep",
    "-k",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Display what would be deleted without deleting anything."),
)
@click.option(
    "--assume-yes",
    "-y",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Assume 'yes' for all questions, not prompting for confirmation."),
)
@click.argument(
    "path",
    required=True,
    type=click.Path(exists=True, dir_okay=True, writable=True),
    default=Path("."),
    metavar=_("<PATH>"),
)
@click.pass_context
@fdocstr(_clean_short_help)
def clean(context: click.Context, keep: bool, assume_yes: bool, path: Path) -> None:
    logger.debug("Entering: keep=%s, assume_yes=%s, path=%s", keep, assume_yes, path)

    # if user indicated a path dir...
    if path:
        # ...check if it is accessible (read and write to delete).
        if check_writable_dir(path):
            # proceed with the cleaning.
            clean_project_path(path, assume_yes)
        else:
            p_error(_("Error: Directory '%s' cannot be accessed or you don't have permission to erase it."), path)
            exit(1)

    else:
        # proceed with the cleaning.
        clean_project(assume_yes)
