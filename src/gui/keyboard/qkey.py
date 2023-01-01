"""A QWidget for rendering a single key."""

from PyQt6.QtWidgets import QPushButton

from src.layout import Key
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
