import logging
from pathlib import Path
from builtins import _, fdocstr

import click

import pneo


# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application settings.
app_config: pneo.AppConfig = pneo.getAppConfig()


# ----------------------------------------------------------------------------
# CLICK: COMMAND SELF
# ----------------------------------------------------------------------------

self_short_help: str = _("Manage the pneo executable installed.")

@click.group(
    invoke_without_command=False,
    short_help=self_short_help
)
@click.pass_context
@fdocstr(self_short_help)
def self(context: click.Context) -> None:
    pass


@self.command()
@click.option(
    "--short", "-s",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Only print the version."),
)
@fdocstr(_("Show current version of installed pneo."))
@click.pass_context
def version(context: click.Context, short: bool) -> None:
    # print(f"short: {short}")
    pass


@self.command()
@click.argument(
    "target_version",
    required=False,
    type=click.STRING,
    metavar=_("<TARGET_VERSION>"),
)
@click.pass_context
@fdocstr(_("Update pneo, installing a specified version, or upgrading to the latest version."))
def upgrade(context: click.Context, target_version: str) -> None:
    # print(f"target_version: {target_version}")
    pass


@self.command()
@click.option(
    "--quiet", "-q",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Specifies quiet mode, not prompting for delete confirmation."),
)
@click.pass_context
@fdocstr(_("Uninstall pneo e remove all files and settings."))
def uninstall(context: click.Context, quiet: bool) -> None:
    # print(f"quiet: {quiet}")
    pass
