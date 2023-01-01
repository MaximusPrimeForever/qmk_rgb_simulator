"""Class for a key."""


from dataclasses import dataclass


@dataclass
class Key:
    """Hold information about a single Key."""

    x: int
    y: int
    width: float = 1.0
    height: float = 1.0
    name: str = ""
