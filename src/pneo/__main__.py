import sys
import logging
from importlib.metadata import version
from builtins import _, fdocstr

import pneo
from pneo.command.invoker import (
    invoker_add,
    invoker_backup,
    invoker_build,
    invoker_check,
    invoker_clean,
    invoker_compile,
    invoker_config,
    invoker_format,
    invoker_init,
    invoker_list,
    invoker_lock,
    invoker_make,
    invoker_package,
    invoker_remove,
    invoker_run,
    invoker_self,
    invoker_tree,
    invoker_venv,
    invoker_version,
    invoker_view,
)

import click


# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application settings.
app_config: pneo.AppConfig = pneo.getAppConfig()


# ----------------------------------------------------------------------------
# ERROR CONSTANTS
# ----------------------------------------------------------------------------

# Possible errors that may occur when executing the application to return in sys.exit():
EXIT_ERROR_CONFIG_LOG = -1
EXIT_ERROR_CONFIG_APP = -2
EXIT_ERROR_INVALID_ARGS = -3
EXIT_ERROR_NO_ARGS = -4
EXIT_ERROR_MAIN = _("Module '__main__.py' cannot be loaded by another module.")

EXIT_SUCCESS = 0  # informs that in fact no error occurred, it was executed successfully.


# ----------------------------------------------------------------------------
# ENTRY-POINT CHECK
# ----------------------------------------------------------------------------

# This module cannot be loaded by another module
if __name__ not in ["__main__", "pneo.__main__"]:
    sys.exit(EXIT_ERROR_MAIN)
# proceeds only if this program was executed as entry-point...


# ----------------------------------------------------------------------------
# MAIN ENTRY-POINT
# ----------------------------------------------------------------------------

# Adds the options '-h' for help and '-V' for version.
CONTEXT_SETTINGS: dict = dict(help_option_names=["-h", "--help"])

@click.group(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.version_option(
    version('pneo'), 
    "--version", "-V",
    message=_("%(prog)s, version %(version)s"),
    help=_("Show the pneo version and exit.")
)
@fdocstr(_("""
Pneo is an all-in-one utility for working with NeoBASIC projects.

It provides source code management, a compiler, a package manager,
and a bundler — streamlining the entire development workflow into
a single tool.
"""))
def cli(context: click.Context) -> None:
    context.ensure_object(dict)
    context.obj["settings"] = app_config


# ----------------------------------------------------------------------------
# CLICK: COMMAND LINE ARGUMENTS
# ----------------------------------------------------------------------------

# Register all commands for click library, more to come...
cli.add_command(invoker_add.add)
cli.add_command(invoker_backup.backup)
cli.add_command(invoker_build.build)
cli.add_command(invoker_check.check)
cli.add_command(invoker_clean.clean)
cli.add_command(invoker_compile.compile)
cli.add_command(invoker_config.config)
cli.add_command(invoker_format.format)
cli.add_command(invoker_init.init)
cli.add_command(invoker_list.list)
cli.add_command(invoker_lock.lock)
cli.add_command(invoker_make.make)
cli.add_command(invoker_package.package)
cli.add_command(invoker_remove.remove)
cli.add_command(invoker_run.run)
cli.add_command(invoker_self.self)
cli.add_command(invoker_tree.tree)
cli.add_command(invoker_venv.venv)
cli.add_command(invoker_version.version)
cli.add_command(invoker_view.view)

# just in case it is not executing with `uv run`.
cli()
