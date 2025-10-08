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
# ENTRY-POINT CHECK
# ----------------------------------------------------------------------------

# This module cannot be loaded by another module.
if __name__ not in ["__main__", "pneo.__main__"]:
    sys.exit(_("Module '__main__.py' cannot be loaded by another module."))
# proceeds only if this program was executed as entry-point...


# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# Now that the app is initialized and checked, we can get the logger and config.
# it is a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# it is a global singleton instance, with application settings.
app_config: pneo.AppConfig = pneo.getAppConfig()


# ----------------------------------------------------------------------------
# MAIN ENTRY-POINT
# ----------------------------------------------------------------------------

# Adds the options '-h' for help and '-V' for version.
CONTEXT_SETTINGS: dict = dict(help_option_names=["-H", "--help"])

APP_ABOUT: str = _("""
Pneo is an all-in-one utility for working with NeoBASIC projects.

It provides source code management, a compiler, a package manager,
and a bundler — streamlining the entire development workflow into
a single tool.
""")

APP_NOTICE: str = _("""
Welcome to NeoBASIC "Developer Preview", version 0.0.1 (build Jan 01 2025 linux/amd64).

Copyright (c) 2025 🇧🇷 Tech4all Developers. All rights reserved unless otherwise stated.
Textual and multimedia content is licensed under CC BY-SA 4.0, feel free to share them.

This is a Free and Open Source Software Ad_hoc; see the project for copying conditions.
There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
""")

@click.group(
    context_settings=CONTEXT_SETTINGS,
    invoke_without_command=True,
)
@click.pass_context
@click.version_option(
    version('pneo'), 
    "-V", "--version",
    message=_("%(prog)s, version %(version)s"),
    help=_("Show the pneo version and exit.")
)
@click.option(
    "-N", "--notice",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Show the legal notice of pneo and exit."),
)
@fdocstr(APP_ABOUT)
def cli(context: click.Context, notice: bool) -> None:
    context.ensure_object(dict)
    context.obj["settings"] = app_config

    if context.invoked_subcommand is None:
        # print the legal notice if required:
        if notice:
            print(APP_NOTICE)

        else: # otherwise, requires any option or command.
            click.echo(context.get_help())
            context.exit()


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
if __name__ == "__main__":
    cli()
