from typing import Any, Optional


class ParseTreeProperty:
    """
    A simple Python equivalent of Java's ParseTreeProperty for ANTLR parse trees.
    Uses a plain dict to associate values with parse tree nodes.
    """

    def __init__(self) -> None:
        self._annotations = {}

    # Original-style API
    def put(self, node: object, value: Any) -> None:
        """Associate `value` with `node`."""
        self._annotations[node] = value

    def get(self, node: object, default: Optional[Any] = None) -> Any:
        """Return value associated with `node`, or `default` if none."""
        return self._annotations.get(node, default)

    def remove_from(self, node: object) -> Optional[Any]:
        """Remove and return the value associated with `node`, or None."""
        return self._annotations.pop(node, None)

    # Helper methods for convenience / readability
    def set_value(self, node: object, value: Any) -> None:
        """Alias for put(node, value)."""
        self.put(node, value)

    def get_value(self, node: object, default: Optional[Any] = None) -> Any:
        """Alias for get(node, default)."""
        return self.get(node, default)
