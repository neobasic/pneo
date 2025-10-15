import logging
from pathlib import Path

import click
from nuke import gettext as _, Settings, fdocstr, p_error
from pneo.command.receiver.receiver_backup import backup_source_file, backup_source

# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()

# ----------------------------------------------------------------------------
# CLICK: COMMAND BACKUP
# ----------------------------------------------------------------------------

_backup_short_help: str = _("Create a zip file with only the source code of current project.")


@click.command(options_metavar=_("<OPTIONS>"), short_help=_backup_short_help)
@click.option(
    "--all",
    "-a",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Includes all files and folders in current project."),
)
@click.option(
    "--force",
    "-f",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Ignore if backup file already exists."),
)
@click.option(
    "--time",
    "-t",
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
@fdocstr(_backup_short_help)
def backup(context: click.Context, all: bool, force: bool, time: bool, file: Path) -> None:
    logger.debug("Entering: all=%s, force=%s, time=%s, file=%s", all, force, time, file)

    # if the file exists, using time flag will generate a different name.
    if file:
        target_file: Path = Path(file)
        if target_file.exists() and not force and not time:
            logger.error("Backup file '%s' already exists, but option '--force' was not used.", file)
            p_error(_("Error: The backup file '%s' already exists. Use the --force option to override it."),
                    file)
            exit(1)

        # proceed with the backup.
        backup_source_file(all, time, target_file)

    else:
        # proceed with the backup.
        backup_source(all, time)
