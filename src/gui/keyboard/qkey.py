"""A QWidget for rendering a single key."""

from PyQt6.QtWidgets import QPushButton

from src.layout import Key, RGB
from src.config.gui import KEY_SIZE


class QKey(QPushButton):
    """QWidget for a single key."""

    def __init__(self, key: Key, *args, **kwargs):
        super(QKey, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)
        self.properties: Key = key

        self.setText(self.properties.name)
        self.setFixedSize(
            int(KEY_SIZE * self.properties.width),
            int(KEY_SIZE * self.properties.height),
        )

        self.show()

    def set_color(self, red: int, green: int, blue: int):
        if red < 0 or green < 0 or blue < 0:
            raise ValueError(
                f"RGB values must be nonnegative. "
                f"Given colors: R:{red}, G:{green}, B:{blue}"
            )

        self.properties.rgb = RGB(red, green, blue)
