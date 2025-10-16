import logging
import os
from pathlib import Path

import click
from nuke import gettext as _, Settings, fdocstr
from nuke.formatters.print_color import p_error
from nuke.utils.shell import check_readable_dir
from pneo.command.receiver.receiver_run import run_script, run_target

# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()

# ----------------------------------------------------------------------------
# CLICK: COMMAND RUN
# ----------------------------------------------------------------------------

_run_short_help: str = _("Execute the binary executable in target directory or a local program.")


@click.command(options_metavar=_("<OPTIONS>"), short_help=_run_short_help)
@click.option(
    "--target",
    "-t",
    required=False,
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
    help=_("Target directory containing the binary executable."),
)
@click.option(
    "--script",
    "-s",
    required=False,
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
    help=_("Run the given source file as a NeoBASIC script."),
)
@click.option(
    "--offline",
    "-o",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Run without accessing the network (disable network access)."),
)
@click.pass_context
@fdocstr(_run_short_help)
def run(context: click.Context, target: Path, script: Path, offline: bool) -> None:
    logger.debug("Entering: target=%s, script=%s, offline=%s", target, script, offline)

    # if user indicated a target dir, check if it is accessible.
    if target and not check_readable_dir(target):
        p_error(_("Error: Target directory '%s' cannot be accessed or you don't have permission to written to it."),
                target)
        exit(1)

    # if user indicated a script file...
    if script:
        # ...check if it exists.
        if os.path.exists(script):
            # proceed with the execution of the script.
            run_script(target, script, offline)

        else:
            p_error(_("Error: Script file '%s' does not exist."), script)
            exit(1)

    else:  # run binary in target
        # proceed with the execution of binary in target.
        run_target(target, offline)
