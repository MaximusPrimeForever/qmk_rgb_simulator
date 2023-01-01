"""Main GUI window."""

import os

from PyQt6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QHBoxLayout,
    QTextEdit,
    QWidget,
    QLabel
)
from PyQt6.QtGui import QIcon, QPixmap

from src.config.strings import PLACEHOLDERS_PATH, ICONS_PATH
from src.gui.keyboard import QKeyboard
from src.layout import KeyboardLayout


class MainWindow(QMainWindow):
    def __init__(self, info_json_path: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QMK RGB Simulator")
        self.setWindowIcon(QIcon(os.path.join(ICONS_PATH, "icon.ico")))

        layout = QHBoxLayout()
        pattern_code = QTextEdit()

        keyboard_layout = KeyboardLayout(info_json_path)
        keyboard = QKeyboard(keyboard_layout)

        layout.addWidget(pattern_code)
        layout.addWidget(keyboard)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
