from enum import Enum
from pathlib import Path
from tabulate import tabulate
import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QWidget
from list import List
from song_module import RepeatMode, Song

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QWidget()
    my_list = List()
    my_list.setupUi(Form)
    Form.show()

    sys.exit(app.exec())