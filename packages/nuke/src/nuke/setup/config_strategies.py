import os
import logging
from pathlib import Path
from importlib import resources
from configparser import ConfigParser
from typing import Dict, List, Optional, Any, Type

import yaml

# ----------------------------------------------------------------------------
# GLOBAL SETTINGS
# ----------------------------------------------------------------------------

# Now that the app is initialized and checked, we can get the logger and config.
# it is a logger instance for the current module.
logger: logging.Logger = logging.getLogger(__name__)


# ----------------------------------------------------------------------------
# CONFIGURATION FILE LOADERS
# ----------------------------------------------------------------------------


class ConfigLoader:
    """Strategy base class for loading config data (INI)."""

    def _extract_config_dict(self, config_parser: ConfigParser) -> Dict:
        """
        Extract all sections and their key/value pairs from a ConfigParser object
        into a nested dictionary, handling unexpected parsing errors gracefully.

        Args:
            config_parser: An initialized and already populated ConfigParser instance.

        Returns:
            A nested dictionary mapping each section name to a dict of key/value pairs.

        Notes:
            - Each section is converted to a dictionary using ConfigParser.items().
            - Any unexpected exception during section extraction is caught and
            reported using `p_error`, but does not interrupt processing.
            - Returns a dictionary containing only successfully parsed sections.
        """

        config_dict: Dict[str, Dict[str, Any]] = {}

        # extract a Dict from the sections and keys/values of config_parser.
        for section in config_parser.sections():
            try:
                # Convert each section to a dict safely.
                config_dict[section] = dict(config_parser.items(section))
            except Exception as e:  # catches almost all unexpected issues
                # Should be rare, but catch any error from extraction.
                logger.error("Failed to parse section '%s': %r", section, e)

        return config_dict

    def load_content_resource(self, anchor: str, filename: str) -> str:
        """Read the content of a file inside the project.

        This function reads the text content of a file located in the
        application configuration package.

        Args:
            anchor (str): The package name (module) where the file resides.
            filename (str): The name of the file to read.

        Returns:
            str: The content of the file as a string.
                 If filename is None or does not exist, returns empty string.
        """

        content: str = ""

        # just to be sure we have valid arguments:
        if not anchor or not filename:
            return content

        try:
            with resources.open_text(anchor, filename) as f:
                content = f.read()

        except Exception as e:  # catches almost all exceptions
            logger.error("Failed to read the content of file '%s' from package '%s': %r", filename, anchor, e)

        return content

    def load_content_file(self, filepath: Optional[Path]) -> str:
        """Read the content of a file outside, from an OS path.

        Args:
            filepath (Path): Path to the text file.

        Returns:
            str: The content of the file as a string.
                 If filepath is None or does not exist, returns empty string.
        """

        content: str = ""

        # if path is null or does not exist, return empty dict.
        if not filepath or not filepath.exists():
            return content

        # read the entire content of the text file as a string.
        try:
            with filepath.open("r", encoding="utf-8") as file:
                content = file.read()

        except Exception as e:  # catches almost all exceptions
            logger.error("Failed to read the content of file '%s': %r", filepath, e)

        return content

    def load_config_str(self, config_content: str) -> Dict[str, Dict[str, Any]]:
        """Parse a configuration from string content.

        This function uses ConfigParser to parse the config content.

        Args:
            config_content (str): The configuration content as string.

        Returns:
            Nested dictionary {section: {key: value, ...}, ...}.
            If config_content is None or empty, returns empty dict.
        """

        config_dict: Dict[str, Dict[str, Any]] = {}

        # just to be sure we have valid arguments:
        if not config_content:
            return config_dict

        # parse the content string through ConfigParser, since it is a valid content.
        config_parser = ConfigParser()

        try:
            config_parser.read_string(config_content)

        except Exception as e:  # catches almost all exceptions
            logger.error("Failed to parse configuration from string content: %r", e)

        # extract a Dict from the sections and keys/values of config_parser.
        config_dict = self._extract_config_dict(config_parser)
        return config_dict

    def load_config_resource(self, anchor: str, filename: str) -> Dict[str, Dict[str, Any]]:
        """Read a configuration file inside the project.

        This function uses ConfigParser to read a file located in the
        application configuration package.

        Args:
            anchor (str): The package name (module) where the configuration resides.
            filename (str): The name of the configuration file to read.

        Returns:
            Nested dictionary {section: {key: value, ...}, ...}.
            If filename is None or does not exist, returns empty dict.
        """

        config_dict: Dict[str, Dict[str, Any]] = {}

        # just to be sure we have valid arguments:
        if not anchor or not filename:
            return config_dict

        # first load the string content of the file.
        content = self.load_content_resource(anchor, filename)
        if not content:
            return config_dict

        # then parse it through ConfigParser, since it is a valid content.
        config_parser = ConfigParser()

        try:
            config_parser.read_string(content)

        except Exception as e:  # catches almost all exceptions
            logger.error("Failed to read config file '%s' from package '%s': %r", filename, anchor, e)

        # extract a Dict from the sections and keys/values of config_parser.
        config_dict = self._extract_config_dict(config_parser)
        return config_dict

    def load_config_file(self, filepath: Optional[Path]) -> Dict[str, Dict[str, Any]]:
        """
        Read the content of a configuration file outside, from an OS path.

        Args:
            filepath (str): Path to the INI config file.

        Returns:
            Nested dictionary {section: {key: value, ...}, ...}.
            If filepath is None or does not exist, returns empty dict.
        """

        config_dict: Dict[str, Dict[str, Any]] = {}

        # if path is null or does not exist, return empty dict.
        if not filepath or not filepath.exists():
            return config_dict

        config_parser = ConfigParser()

        try:
            # `.read()` returns a list of files that it successfully read.
            read_files: List[str] = config_parser.read(filepath)

            # Then we check if our file is in that list.
            if not read_files or os.fspath(filepath) not in read_files:
                # File exists but nothing was read (empty or unreadable)
                return config_dict

        except Exception as e:  # catches almost all exceptions
            logger.error("Failed to read config file '%s': %r", filepath, e)

        # extract a Dict from the sections and keys/values of config_parser.
        config_dict = self._extract_config_dict(config_parser)
        return config_dict


class YamlConfigLoader(ConfigLoader):
    """Strategy class for loading config data of type YAML."""

    def load_config_str(self, config_content: str) -> Dict[str, Dict[str, Any]]:
        """Parse a configuration from string content of type YAML.

        This function uses pyyml to parse the config content.

        Args:
            config_content (str): The configuration content as string.

        Returns:
            Nested dictionary {section: {key: value, ...}, ...}.
            If config_content is None or empty, returns empty dict.
        """

        config_dict: Dict[str, Dict[str, Any]] = {}

        # just to be sure we have valid arguments:
        if not config_content:
            return config_dict

        # parse the content string through the YAML parser, since it is a valid content.
        try:
            config_dict = yaml.safe_load(config_content)

        except Exception as e:  # catches almost all exceptions
            logger.error("Failed to parse YAML configuration from string content: %r", e)

        return config_dict

    def load_config_resource(self, anchor: str, filename: str) -> Dict[str, Dict[str, Any]]:
        """Read a configuration file of type YAML inside the project.

        Args:
            anchor (str): The package name (module) where the configuration resides.
            filename (str): The name of the configuration file to read.

        Returns:
            Nested dictionary {section: {key: value, ...}, ...}.
            If filename is None or does not exist, returns empty dict.
        """

        config_dict: Dict[str, Dict[str, Any]] = {}

        # just to be sure we have valid arguments:
        if not anchor or not filename:
            return config_dict

        # first load the string content of the file.
        content = self.load_content_resource(anchor, filename)

        # if the file is empty, we can exit by now.
        if not content:
            return config_dict

        # then parse it through the YAML parser, since it is a valid content.
        try:
            config_dict = yaml.safe_load(content)

        except Exception as e:  # catches almost all exceptions
            logger.error("Failed to read config file '%s' from package '%s': %r", filename, anchor, e)

        return config_dict

    def load_config_file(self, filepath: Optional[Path]) -> Dict[str, Dict[str, Any]]:
        """
        Read the content of a configuration file of type YAML outside, from an OS path.

        Args:
            filepath (str): Path to the YAML config file.
                            If None or file does not exist, returns empty dict.

        Returns:
            Nested dictionary {section: {key: value, ...}, ...}.
            If filepath is None or does not exist, returns empty dict.
        """

        config_dict: Dict[str, Dict[str, Any]] = {}

        # if path is null or does not exist, return empty dict.
        if not filepath or not filepath.exists():
            return config_dict

        # first, read the entire content of a text file as a string.
        content: str = ""
        try:
            with filepath.open("r", encoding="utf-8") as file:
                content = file.read()

            # if the file is empty, we can exit by now.
            if not content:
                return config_dict

        except Exception as e:  # catches almost all exceptions
            logger.error("Failed to read config file '%s': %r", filepath, e)

        # then parse it through the YAML parser, since it is a valid content.
        try:
            config_dict = yaml.safe_load(content)

        except Exception as e:  # catches almost all exceptions
            logger.error("Failed to read config file '%s': %r", filepath, e)

        return config_dict


# ----------------------------------------------------------------------------
# LOADING STRATEGIES
# ----------------------------------------------------------------------------

_strategies: Dict[str, Type[ConfigLoader]] = {
    "conf": ConfigLoader,
    "ini": ConfigLoader,
    "yaml": YamlConfigLoader,
}


def get_strategy(config_ext: Optional[str] = None) -> ConfigLoader:
    """
    Return a configuration loader strategy based on the file extension.

    This function looks up the appropriate ConfigLoader subclass for the given
    configuration file extension. If no specific strategy is found, it defaults
    to the base ConfigLoader.

    Args:
        config_ext (str): The configuration file extension (e.g. 'ini', 'yaml', 'json').

    Returns:
        ConfigLoader: An instance of the corresponding loader class for the given extension.
    """

    ext: str = config_ext if config_ext else "conf"

    loader_class: Type[ConfigLoader] = _strategies.get(ext, ConfigLoader)
    return loader_class()
