from enum import Enum
from pathlib import Path

class RepeatMode(Enum):
        
    no_repeat = 0
    repeat_one = 1
    repeat_all = 2

class Song():
    def __init__(self, title, artistName, duration, filePath, genre):
        self.title = title()
        self.artistName = artistName()
        self.duration = duration()
        self.filePath = filePath()
        self.genre = genre()

    def _getTitle(self):
        pass

    def _getArtistName(self):
        pass

    def _getFilePath(self, filepath):
        
        self.filePath = Path("music")
        
        
    def _getGenre(self):
        pass



    def getDisplayName(self):
        pass

    def _getDuration(self):
        pass