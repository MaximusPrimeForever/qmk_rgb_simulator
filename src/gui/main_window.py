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

from src.config.strings import APP_TITLE, ICONS_PATH
from src.gui.keyboard import QKeyboard
from src.layout import Matrix


class MainWindow(QMainWindow):
    def __init__(self, info_json_path: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle(APP_TITLE)
        self.setWindowIcon(QIcon(os.path.join(ICONS_PATH, "icon.ico")))

        layout = QHBoxLayout()
        pattern_code = QTextEdit()

        keyboard_layout = Matrix(info_json_path)
        keyboard = QKeyboard(keyboard_layout)

        layout.addWidget(pattern_code)
        layout.addWidget(keyboard)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
