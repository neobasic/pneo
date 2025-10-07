import logging
from pathlib import Path
from builtins import _, fdocstr

import pneo

import click


# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application settings.
app_config: pneo.AppConfig = pneo.getAppConfig()


# ----------------------------------------------------------------------------
# CLICK: COMMAND BACKUP
# ----------------------------------------------------------------------------

backup_short_help: str = _("Create a zip file with only the source code of current project.")

@click.command(
    options_metavar=_("<OPTIONS>"),
    short_help=backup_short_help
)
@click.option(
    "--all", "-a",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Includes all files and folders in current project."),
)
@click.option(
    "--force", "-f",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Ignore if backup file already exists."),
)
@click.option(
    "--time", "-t",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Includes the current time in file name."),
)
@click.argument(
    "file",
    required=False,
    type=click.Path(exists=False, file_okay=True, dir_okay=True, writable=True),
    metavar=_("<FILE>"),
)
@click.pass_context
@fdocstr(backup_short_help)
def backup(context: click.Context, all: bool, force: bool, time: bool, file: Path) -> None:
    # print(f"all: {all}, force: {force}, time: {time}, file: {file}")
    pass
