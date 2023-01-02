"""Class for a key."""

from random import randint
from dataclasses import dataclass


@dataclass
class RGB:
    r: int
    g: int
    b: int

    def randomize(self):
        self.r = randint(0, 255)
        self.g = randint(0, 255)
        self.b = randint(0, 255)


@dataclass
class Key:
    """Hold information about a single Key."""

    x: int
    y: int
    width: float = 1.0
    height: float = 1.0
    rgb: RGB = RGB(255, 255, 255)
    name: str = ""
