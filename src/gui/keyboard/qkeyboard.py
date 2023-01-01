"""Draw a full keyboard."""

from typing import List

from PyQt6.QtWidgets import QWidget

from src.gui.keyboard import QKey
from src.layout import Key, KeyboardLayout
from src.config.gui import PADDING_BETWEEN_KEYS, KEY_SIZE, KEYBOARD_MARGIN


class QKeyboard(QWidget):
    """QWidget for a full keyboard."""

    def __init__(self, keyboard_layout: KeyboardLayout, *args, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)
        self.keyboard_layout = keyboard_layout

        width_total = self.keyboard_layout.width_total * KEY_SIZE
        height_total = self.keyboard_layout.height_total * KEY_SIZE

        self.setMinimumSize(
            int(width_total + KEYBOARD_MARGIN),
            int(height_total + KEYBOARD_MARGIN)
        )
        self._place_keys()
        self.show()

    def _place_keys(self):
        for row in self.keyboard_layout.matrix:
            key: Key
            for key in row:
                if key is None:
                    continue

                key_button = QKey(key, parent=self)
                key_button.move(
                    int(PADDING_BETWEEN_KEYS + key.x * KEY_SIZE),
                    int(PADDING_BETWEEN_KEYS + key.y * KEY_SIZE)
                )
