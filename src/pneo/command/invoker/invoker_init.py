import logging
from pathlib import Path

import click
from nuke import gettext as _, Settings, fdocstr
from nuke.formatters.print_color import p_error
from nuke.utils.shell import make_accessible_dir
from pneo.command.receiver.receiver_init import ProjectType, initialize_project

# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()

# ----------------------------------------------------------------------------
# CLICK: COMMAND INIT
# ----------------------------------------------------------------------------

_init_short_help: str = _("Create a new NeoBASIC project in an existing <PATH> directory. [default: .]")


@click.command(options_metavar=_("<OPTIONS>"), short_help=_init_short_help)
@click.option(
    "--name",
    "-n",
    required=False,
    type=click.STRING,
    help=_("The name of the project."),
)
@click.option(
    "--app",
    "-a",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Create a project for an application."),
)
@click.option(
    "--lib",
    "-l",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Create a project for a library."),
)
@click.argument(
    "path",
    required=True,
    type=click.Path(exists=False, dir_okay=True, writable=True),
    default=Path("."),
    metavar=_("<PATH>"),
)
@click.pass_context
@fdocstr(_init_short_help)
def init(context: click.Context, name: str, app: bool, lib: bool, path: Path) -> None:
    logger.debug("Entering: name=%s, app=%s, lib=%s, path=%s", name, app, lib, path)

    # if user indicated a path dir...
    if path:
        # ...check if it is accessible.
        if not make_accessible_dir(path):
            p_error(_("Error: Directory '%s' cannot be accessed or you don't have permission to written to it."),
                    path)
            exit(1)

    # if did not provide the name, extract from path.
    prj_name: str = name if name else Path.cwd().name or 'root'  # just in case we're in '/'

    # app is the default project type
    ptype: ProjectType = ProjectType.APP

    # can't use --app and --lib together.
    if app and lib:
        logger.error("Used both options '--app' and '--lib' in command INIT.")
        p_error(_("Error: The flags <*'--app'*> and <*'--lib'*> are mutually exclusive; choose only one."))
        exit(1)

    elif lib:
        ptype = ProjectType.LIB

    # proceed with the initialization.
    initialize_project(prj_name, path, ptype)
