from enum import Enum
from pathlib import Path
from tabulate import tabulate
import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide6.QtGui import QColor
from list import List

class RepeatMode(Enum):
        
    no_repeat = 0
    repeat_one = 1
    repeat_all = 2

class Song(List): 
    from tabulate import tabulate
    def __init__(self):
        self.base_dir = Path(__file__).resolve().parent
        self.song_path = self.base_dir / "music"

    def _loadDataTable(self):
        song_list =  self._getSongTitles()
        column_index = 0
        header_label = "Song Title"
        self.tableWidget.setRowCount(len(song_list))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setHorizontalHeaderLabels([header_label])
        
        for row, item_text in enumerate(song_list):
            item = QTableWidgetItem(str(song_list))
            self.tableWidget.setItem(row, 0, item)
        self.tableWidget.resizeColumnsToContents()
        
    def _getSongTitles(self):
        song_list = []
        for song_item in self.song_path.iterdir():
            if song_item.is_file():
                if song_item.suffix == ".mp3":
                    song_list.append(song_item.stem)
        return song_list        
    
    def song__queue(self, title):
        
        title = self.title
        
        for song_item in self.song_path.iterdir():
            if song_item.is_file() and title.is_exist():
                continue
        
    def _getGenre(self):
        pass



    def getDisplayName(self):
        pass

    def _getDuration(self):
        pass
