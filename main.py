"""Main launcher."""

import sys

from PyQt6.QtWidgets import QApplication
from src.gui.main_window import MainWindow


if __name__ == "__main__":
    app = QApplication([])

    if len(sys.argv) != 2:
        sys.exit("Proive path to keyboard info.json file.")

    window = MainWindow(sys.argv[1])
    window.show()

    app.exec()
