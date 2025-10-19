import logging
import sys
from importlib.metadata import version
from pathlib import Path

import colorama

import click
from nuke import gettext as _, Settings, fdocstr, p_info, p_error
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
    invoker_lint,
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

# ----------------------------------------------------------------------------
# ENTRY-POINT CHECK
# ----------------------------------------------------------------------------

# This module cannot be loaded by another module.
if __name__ not in ["__main__", "pneo.__main__"]:
    p_error(_("Module '__main__.py' cannot be loaded by another module."))
    sys.exit(1)
# proceeds only if this program was executed as entry-point...

# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# Now that the app is initialized and checked, we can get the logger and config.
# it is a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# it is a global singleton instance, with application setup.
settings: Settings = Settings.get_instance()

# colorama setup: Automatically reset styles after each print
colorama.init(autoreset=True)

# ----------------------------------------------------------------------------
# MAIN ENTRY-POINT
# ----------------------------------------------------------------------------

APP_ABOUT: str = _("""
Pneo is an all-in-one utility for working with NeoBASIC projects.

It provides source code management, a compiler, a package manager,
and a bundler — streamlining the entire development workflow into
a single tool.
"""
                   )

APP_NOTICE: str = _("""
Welcome to <*NeoBASIC "Developer Preview"*>, <*version 0.0.1*> (build Jan 01 2025 linux/amd64).

<*NeoBASIC*> is a simple and statically-typed programming language. It is designed for 
educational purposes and to be easy to implement. It is also intended to be fast, but
not to be used in production, yet.

<*NeoBASIC*> is a work in progress and may not have all the features you expect.
For more information, visit <*https://www.neobasic.org/*>

<*Copyright (c) 2025 🇧🇷 Tech4all Developers*>. All rights reserved unless otherwise stated.
Textual and multimedia content is licensed under <*CC BY-SA 4.0*>, feel free to share them.

This is a Free and Open Source Software Ad_hoc; see the project for copying conditions.
There is <*NO*> warranty; not even for <*MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE*>.
"""
                    )

# Adds the options '-h' for help and '-V' for version.
CONTEXT_SETTINGS: dict = dict(help_option_names=["-h", "--help"])


@click.group(
    context_settings=CONTEXT_SETTINGS,
    invoke_without_command=True,
)
@click.version_option(
    version("pneo"),
    "-V", "--version",
    message=_("%(prog)s, version %(version)s"),
    help=_("Show the pneo version and exit."),
)
@click.option(
    "-N", "--notice",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Show the legal notice of pneo and exit."),
)
@click.option(
    "-v", "--verbose",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Use verbose output on console, about what pneo is doing."),
)
@click.option(
    "-cc", "--color",
    required=False,
    type=click.Choice(
        ["auto", "never", "black", "blue", "cyan",
         "green", "magenta", "red", "white", "yellow"],
        case_sensitive=False
    ),
    default="auto",
    help=_("Control the use of color in output."),
)
@click.option(
    "-np", "--no-progress",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Hide all progress outputs. For example, spinners or progress bars."),
)
@click.option(
    "-off", "--offline",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Disable network access. "
           "When disabled, pneo will only use locally cached data and locally available files."),
)
@click.option(
    "-qq", "--quiet",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Use quiet output. "
           "Enable a silent mode in which pneo will write no output to stdout."),
)
@click.option(
    "-cf", "--config-file",
    required=False,
    type=click.Path(exists=True, file_okay=True, dir_okay=True),
    help=_("The path to a 'pneo.conf' file to use for configuration."),
)
@click.option(
    "-cs", "--config-setting",
    required=False,
    type=click.STRING,
    help=_("Setting to use, overriding the current configuration, specified as KEY=VALUE pair. "
           "For two or more settings, use '' as delimiter and `;` as a separator without spaces."),
)
@click.option(
    "-dd", "--directory",
    required=False,
    type=click.Path(exists=True, file_okay=True, dir_okay=True),
    help=_("Change to the given directory prior to running the command. "
           "Relative paths are resolved with the given directory as the base."),
)
@click.option(
    "-pp", "--project",
    required=False,
    type=click.STRING,
    help=_("Run the command within the given project directory."),
)
@click.pass_context
@fdocstr(APP_ABOUT)
def cli(context: click.Context, notice: bool, verbose: bool, color: str, no_progress: bool, offline: bool, quiet: bool,
        config_setting: str, config_file: Path, directory: Path, project: str):
    logger.debug("Entering: notice=%s, verbose=%s", notice, verbose)

    # save all global options, to be used in commands processing.
    context.ensure_object(dict)
    context.obj["verbose"] = verbose
    context.obj["color"] = color
    context.obj["no_progress"] = no_progress
    context.obj["offline"] = offline
    context.obj["quiet"] = quiet

    if config_setting: context.obj["config_setting"] = config_setting
    if config_file: context.obj["config_file"] = config_file
    if directory: context.obj["directory"] = directory
    if project: context.obj["project"] = project

    # now there is a valid context to be stored in global setup:
    settings.ctx = context

    # calling pneo with no commands means showing version, notice, or help.
    if not context.invoked_subcommand:
        # print the legal notice if required:
        if notice:
            p_info(APP_NOTICE)

        else:  # otherwise, requires any option or command.
            click.echo(context.get_help())
            context.exit()


# ----------------------------------------------------------------------------
# CLICK: COMMAND LINE ARGUMENTS
# ----------------------------------------------------------------------------

# Register all commands for click library, more to come...
cli.add_command(invoker_add.add)  # type: ignore
cli.add_command(invoker_backup.backup)  # type: ignore
cli.add_command(invoker_build.build)  # type: ignore
cli.add_command(invoker_check.check)  # type: ignore
cli.add_command(invoker_clean.clean)  # type: ignore
cli.add_command(invoker_compile.compiler)  # type: ignore
cli.add_command(invoker_config.config)  # type: ignore
cli.add_command(invoker_format.formatter)  # type: ignore
cli.add_command(invoker_init.init)  # type: ignore
cli.add_command(invoker_lint.lint)  # type: ignore
cli.add_command(invoker_list.lister)  # type: ignore
cli.add_command(invoker_lock.lock)  # type: ignore
cli.add_command(invoker_make.make)  # type: ignore
cli.add_command(invoker_package.package)  # type: ignore
cli.add_command(invoker_remove.remove)  # type: ignore
cli.add_command(invoker_run.run)  # type: ignore
cli.add_command(invoker_self.self)  # type: ignore
cli.add_command(invoker_tree.tree)  # type: ignore
cli.add_command(invoker_venv.venv)  # type: ignore
cli.add_command(invoker_version.version)  # type: ignore
cli.add_command(invoker_view.view)  # type: ignore
logger.debug("All 20 commands registered in click library.")

# just in case it is not executing with `uv run`.
if __name__ == "__main__":
    logger.debug("Tracing: Application was started through a run script.")
    cli()
