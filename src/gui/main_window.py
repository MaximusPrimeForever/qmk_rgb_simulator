"""Main GUI window."""

from PyQt6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QHBoxLayout,
    QTextEdit,
    QWidget
)
from PyQt6.QtGui import QPalette, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMK RGB Simulator")

        layout = QHBoxLayout()
        pattern_code = QTextEdit()

        keyboard = QPushButton("ESC")

        layout.addWidget(pattern_code)
        layout.addWidget(keyboard)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
