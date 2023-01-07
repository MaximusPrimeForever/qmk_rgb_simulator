"""Draw a full keyboard."""

from PyQt6.QtWidgets import QWidget

from src.gui.keyboard import QKey
from src.layout import Key, Matrix
from src.config.gui import PADDING_BETWEEN_KEYS, KEY_SIZE, KEYBOARD_MARGIN


class QKeyboard(QWidget):
    """QWidget for a full keyboard."""

    def __init__(self, keyboard_layout: Matrix, *args, **kwargs):
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
        row_counter = 0
        for row in self.keyboard_layout._array:
            key: Key
            col_counter = 0

            for key in row:
                col_counter += 1
                if key is None:
                    continue

                key_button = QKey(key, parent=self)
                key_button.move(
                    int(PADDING_BETWEEN_KEYS * col_counter + key.x * KEY_SIZE),
                    int(PADDING_BETWEEN_KEYS * row_counter + key.y * KEY_SIZE)
                )
            row_counter += 1
