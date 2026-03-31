from enum import Enum
from pathlib import Path
from tabulate import tabulate
import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from list import List
from song_module import RepeatMode, Song
from player_gui.main_player import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    Form = Song()
    Form.show()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

# app = QApplication(sys.argv)

# loader = QUiLoader()
# ui_file = QFile(str(Path(__file__).with_name("untitled.ui")))
# ui_file.open(QIODevice.ReadOnly)
# window = loader.load(ui_file)
# ui_file.close()

# window.show()
# sys.exit(app.exec())
