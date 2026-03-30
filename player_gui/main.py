import sys
from pathlib import Path

from PySide6.QtCore import QTime, QUrl
from PySide6.QtGui import QIcon
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow

from MusicWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.muted = True
        self.audioVolumeLevel = 70

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.player = QMediaPlayer()
        self.audio = QAudioOutput()

        self._configure_window()
        self._configure_player()
        self._connect_signals()

    def _configure_window(self):
        self.setWindowTitle('Music Player')
        self.setWindowIcon(QIcon(":/icons/play.png"))
        self.statusBar().showMessage('Open a track from File to begin.')

        self.ui.toolButtonPlay.setEnabled(False)
        self.ui.horizontalSliderVolume.setValue(self.audioVolumeLevel)
        self.ui.horizontalSliderVolume.setSingleStep(1)
        self.ui.horizontalSliderVolume.setPageStep(5)
        self.ui.horizontalSliderPlay.setSingleStep(1000)

        self.ui.actionOpen_Music.setStatusTip('Open a local audio file')
        self.ui.toolButtonPlay.setToolTip('Play or resume')
        self.ui.toolButtonPause.setToolTip('Pause')
        self.ui.toolButtonStop.setToolTip('Stop')
        self.ui.toolButtonVolume.setToolTip('Mute or unmute')
        self.ui.horizontalSliderPlay.setToolTip('Seek through the current track')
        self.ui.horizontalSliderVolume.setToolTip('Adjust volume')

    def _configure_player(self):
        self.player.setAudioOutput(self.audio)
        self.audio.setVolume(self.audioVolumeLevel / 100)

    def _connect_signals(self):
        self.ui.actionOpen_Music.triggered.connect(self.open_music)
        self.ui.toolButtonPlay.clicked.connect(self.play_music)
        self.ui.horizontalSliderVolume.sliderMoved.connect(self.volume_slider_changed)
        self.ui.horizontalSliderPlay.sliderMoved.connect(self.play_slider_changed)
        self.ui.toolButtonPause.clicked.connect(self.pause_btn)
        self.ui.toolButtonStop.clicked.connect(self.stop_btn)
        self.ui.toolButtonVolume.clicked.connect(self.volume_mute)

        self.player.positionChanged.connect(self.position_changed)
        self.player.durationChanged.connect(self.duration_changed)

    def open_music(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Music")

        if fileName != '':
            self.player.setSource(QUrl.fromLocalFile(fileName))
            self.ui.toolButtonPlay.setEnabled(True)
            self.statusBar().showMessage(f"Loaded: {Path(fileName).name}")

    def play_music(self):
        print('Called play music')
        if self.player.mediaStatus == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    def position_changed(self, position):
        if(self.ui.horizontalSliderPlay.maximum() != self.player.duration()):
            self.ui.horizontalSliderPlay.setMaximum(self.player.duration())

        self.ui.horizontalSliderPlay.setValue(position)

        seconds = (position / 1000) % 60
        minutes = (position / 60000) % 60
        hours = (position / 2600000) % 24

        time = QTime(hours, minutes, seconds)
        self.ui.labelTimer.setText(time.toString())

    def duration_changed(self, duration):
        self.ui.horizontalSliderPlay.setRange(0, duration)

    def volume_slider_changed(self, position):
        self.audioVolumeLevel = position
        self.audio.setVolume(position / 100)

    def play_slider_changed(self, position):
        self.player.setPosition(position)

    def pause_btn(self):
        self.player.pause()

    def stop_btn(self):
        self.player.stop()

    def volume_mute(self):
        if(self.muted):
            self.audio.setMuted(True)
            self.ui.horizontalSliderVolume.setValue(0)
            self.ui.toolButtonVolume.setIcon(QIcon(":/icons/mute.png"))
            self.muted = False
        else:
            self.audio.setMuted(False)
            self.ui.horizontalSliderVolume.setValue(self.audioVolumeLevel)
            self.ui.toolButtonVolume.setIcon(QIcon(":/icons/volume.png"))
            self.muted = True


app = QApplication(sys.argv)
app.setStyle("Fusion")
window = MainWindow()
window.show()
sys.exit(app.exec())
