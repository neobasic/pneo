import logging
from pathlib import Path

import click

from nuke import gettext as _, ngettext as _n, Settings, fdocstr, echo, p_trace, p_debug, p_info, p_warn, p_error, p_fatal


# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# gets a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)

# singleton instance with application setup.
settings: Settings = Settings.get_instance()


# ----------------------------------------------------------------------------
# CLICK: COMMAND SELF
# ----------------------------------------------------------------------------

_self_short_help: str = _("Manage the pneo executable installed.")


@click.group(invoke_without_command=False, short_help=_self_short_help)
@click.pass_context
@fdocstr(_self_short_help)
def self(context: click.Context) -> None:
    pass


@self.command()
@click.option(
    "--short",
    "-s",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Only print the version."),
)
@click.pass_context
@fdocstr(_("Show current version of installed pneo."))
def version(context: click.Context, short: bool) -> None:
    logger.debug("Entering: short=%s", short)
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
    logger.debug("Entering: target_version=%s", target_version)
    pass


@self.command()
@click.option(
    "--assume-yes",
    "-y",
    required=False,
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=_("Assume 'yes' for all questions, not prompting for confirmation."),
)
@click.pass_context
@fdocstr(_("Uninstall pneo e remove all files and setup."))
def uninstall(context: click.Context, assume_yes: bool) -> None:
    logger.debug("Entering: assume_yes=%s", assume_yes)

    pass
