from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QMenu,
    QMenuBar,
    QSizePolicy,
    QSlider,
    QStatusBar,
    QToolButton,
    QVBoxLayout,
    QWidget,
)

from . import resources


WINDOW_SIZE = QSize(680, 400)
WINDOW_MINIMUM_SIZE = QSize(680, 400)
BUTTON_SIZE = QSize(48, 48)
PRIMARY_BUTTON_SIZE = QSize(58, 58)
BUTTON_ICON_SIZE = QSize(22, 22)
PRIMARY_ICON_SIZE = QSize(26, 26)

APP_STYLESHEET = """
QMainWindow,
QWidget#centralwidget {
    background-color: #eff2f0;
    color: #1f2622;
    font-family: "Segoe UI";
}

QMenuBar {
    background-color: transparent;
    border: none;
    color: #405048;
    padding: 8px 14px 0 14px;
}

QMenuBar::item {
    background: transparent;
    border-radius: 10px;
    margin-right: 6px;
    padding: 6px 12px;
}

QMenuBar::item:selected {
    background-color: #e1e6e3;
    color: #18201c;
}

QMenu {
    background-color: #ffffff;
    border: 1px solid #d7dfda;
    border-radius: 12px;
    color: #202823;
    padding: 8px;
}

QMenu::item {
    border-radius: 8px;
    padding: 8px 28px 8px 12px;
}

QMenu::item:selected {
    background-color: #eef2ef;
}

QStatusBar {
    background-color: #f5f7f5;
    border-top: 1px solid #d7dfda;
    color: #69756f;
}

QStatusBar::item {
    border: none;
}

QFrame#playerCard {
    background-color: #ffffff;
    border: 1px solid #d7dfda;
    border-radius: 24px;
}

QFrame#timerCard,
QFrame#playbackGroup,
QFrame#volumeGroup {
    background-color: #f7f9f8;
    border: 1px solid #dde4df;
    border-radius: 18px;
}

QLabel#labelHeading {
    color: #17201b;
    font-size: 22px;
    font-weight: 600;
}

QLabel#labelSubtitle,
QLabel#labelTimerCaption,
QLabel#labelVolumeText {
    color: #74807a;
    font-size: 10px;
    font-weight: 600;
}

QLabel#labelTimer {
    color: #17201b;
    font-family: "Consolas";
    font-size: 18px;
    font-weight: 600;
}

QToolButton {
    background-color: #f0f4f1;
    border: 1px solid #d7dfda;
    border-radius: 16px;
    padding: 8px;
}

QToolButton:hover {
    background-color: #e8ede9;
    border-color: #c7d1cb;
}

QToolButton:pressed {
    background-color: #dfe6e1;
}

QToolButton:disabled {
    background-color: #f5f7f5;
    border-color: #e6ece8;
}

QToolButton#toolButtonPlay {
    background-color: #dce6de;
    border-color: #c2d0c7;
}

QToolButton#toolButtonPlay:hover {
    background-color: #d3dfd7;
}

QToolButton#toolButtonVolume {
    background-color: #ffffff;
}

QSlider::groove:horizontal {
    background-color: #dee4e0;
    border-radius: 4px;
    height: 8px;
}

QSlider::sub-page:horizontal {
    background-color: #8aa08f;
    border-radius: 4px;
}

QSlider::handle:horizontal {
    background-color: #17201b;
    border: none;
    border-radius: 8px;
    margin: -6px 0;
    width: 16px;
}

QSlider#horizontalSliderPlay::groove:horizontal {
    height: 10px;
}

QSlider#horizontalSliderPlay::sub-page:horizontal {
    background-color: #5d7667;
}
"""


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")

        MainWindow.resize(WINDOW_SIZE.width(), WINDOW_SIZE.height())
        MainWindow.setMinimumSize(WINDOW_MINIMUM_SIZE)
        MainWindow.setStyleSheet(APP_STYLESHEET)

        self.actionOpen_Music = QAction(MainWindow)
        self.actionOpen_Music.setObjectName("actionOpen_Music")
        self.actionOpen_Playlist = QAction(MainWindow)
        self.actionOpen_Playlist.setObjectName("actionOpen_Playlist")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(24, 18, 24, 22)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.playerCard = QFrame(self.centralwidget)
        self.playerCard.setObjectName("playerCard")
        self.playerCard.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))

        self.verticalLayout = QVBoxLayout(self.playerCard)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(26, 24, 26, 24)
        self.verticalLayout.setSpacing(20)

        self.headerLayout = QHBoxLayout()
        self.headerLayout.setObjectName("headerLayout")
        self.headerLayout.setSpacing(18)

        self.titleLayout = QVBoxLayout()
        self.titleLayout.setObjectName("titleLayout")
        self.titleLayout.setSpacing(4)

        self.labelSubtitle = QLabel(self.playerCard)
        self.labelSubtitle.setObjectName("labelSubtitle")
        self.titleLayout.addWidget(self.labelSubtitle)

        self.labelHeading = QLabel(self.playerCard)
        self.labelHeading.setObjectName("labelHeading")
        self.titleLayout.addWidget(self.labelHeading)

        self.headerLayout.addLayout(self.titleLayout, 1)

        self.timerCard = QFrame(self.playerCard)
        self.timerCard.setObjectName("timerCard")
        self.timerLayout = QVBoxLayout(self.timerCard)
        self.timerLayout.setContentsMargins(14, 10, 14, 10)
        self.timerLayout.setSpacing(2)

        self.labelTimerCaption = QLabel(self.timerCard)
        self.labelTimerCaption.setObjectName("labelTimerCaption")
        self.timerLayout.addWidget(self.labelTimerCaption)

        self.labelTimer = QLabel(self.timerCard)
        self.labelTimer.setObjectName("labelTimer")
        self.labelTimer.setAlignment(Qt.AlignCenter)
        self.labelTimer.setMinimumWidth(96)
        self.timerLayout.addWidget(self.labelTimer)

        self.headerLayout.addWidget(self.timerCard, 0, Qt.AlignTop)
        self.verticalLayout.addLayout(self.headerLayout)

        self.progressLayout = QHBoxLayout()
        self.progressLayout.setObjectName("progressLayout")
        self.progressLayout.setSpacing(12)

        self.horizontalSliderPlay = QSlider(self.playerCard)
        self.horizontalSliderPlay.setObjectName("horizontalSliderPlay")
        self.horizontalSliderPlay.setCursor(Qt.PointingHandCursor)
        self.horizontalSliderPlay.setOrientation(Qt.Horizontal)
        self.horizontalSliderPlay.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.horizontalSliderPlay.setMinimumHeight(24)
        self.progressLayout.addWidget(self.horizontalSliderPlay)

        self.verticalLayout.addLayout(self.progressLayout)

        self.controlsLayout = QHBoxLayout()
        self.controlsLayout.setObjectName("controlsLayout")
        self.controlsLayout.setSpacing(18)

        self.playbackGroup = QFrame(self.playerCard)
        self.playbackGroup.setObjectName("playbackGroup")
        self.playbackGroup.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.horizontalLayout_2 = QHBoxLayout(self.playbackGroup)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.horizontalLayout_2.setSpacing(10)

        self.toolButtonPlay = self._create_button(
            self.playbackGroup,
            "toolButtonPlay",
            ":/icons/play.png",
            PRIMARY_BUTTON_SIZE,
            PRIMARY_ICON_SIZE,
        )
        self.horizontalLayout_2.addWidget(self.toolButtonPlay)

        self.toolButtonPause = self._create_button(
            self.playbackGroup,
            "toolButtonPause",
            ":/icons/pause.png",
            BUTTON_SIZE,
            BUTTON_ICON_SIZE,
        )
        self.horizontalLayout_2.addWidget(self.toolButtonPause)

        self.toolButtonStop = self._create_button(
            self.playbackGroup,
            "toolButtonStop",
            ":/icons/stop.png",
            BUTTON_SIZE,
            BUTTON_ICON_SIZE,
        )
        self.horizontalLayout_2.addWidget(self.toolButtonStop)

        self.controlsLayout.addWidget(self.playbackGroup, 0, Qt.AlignLeft | Qt.AlignVCenter)
        self.controlsLayout.addStretch(1)

        self.volumeGroup = QFrame(self.playerCard)
        self.volumeGroup.setObjectName("volumeGroup")
        self.volumeGroup.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed))
        self.volumeLayout = QHBoxLayout(self.volumeGroup)
        self.volumeLayout.setContentsMargins(14, 12, 14, 12)
        self.volumeLayout.setSpacing(12)

        self.labelVolumeText = QLabel(self.volumeGroup)
        self.labelVolumeText.setObjectName("labelVolumeText")
        self.volumeLayout.addWidget(self.labelVolumeText)

        self.toolButtonVolume = self._create_button(
            self.volumeGroup,
            "toolButtonVolume",
            ":/icons/volume.png",
            QSize(42, 42),
            QSize(20, 20),
        )
        self.volumeLayout.addWidget(self.toolButtonVolume)

        self.horizontalSliderVolume = QSlider(self.volumeGroup)
        self.horizontalSliderVolume.setObjectName("horizontalSliderVolume")
        self.horizontalSliderVolume.setCursor(Qt.PointingHandCursor)
        self.horizontalSliderVolume.setOrientation(Qt.Horizontal)
        self.horizontalSliderVolume.setRange(0, 100)
        self.horizontalSliderVolume.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.horizontalSliderVolume.setMinimumWidth(140)
        self.horizontalSliderVolume.setMaximumWidth(220)
        self.horizontalSliderVolume.setMinimumHeight(24)
        self.volumeLayout.addWidget(self.horizontalSliderVolume)

        self.controlsLayout.addWidget(self.volumeGroup, 0, Qt.AlignRight | Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.controlsLayout)

        self.verticalLayout_2.addWidget(self.playerCard)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, WINDOW_SIZE.width(), 30))
        self.menubar.setNativeMenuBar(False)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setSizeGripEnabled(False)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen_Music)
        self.menuFile.addAction(self.actionOpen_Playlist)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def _create_button(self, parent, object_name, icon_path, button_size, icon_size):
        button = QToolButton(parent)
        button.setObjectName(object_name)
        button.setCursor(Qt.PointingHandCursor)
        button.setIcon(self._icon(icon_path))
        button.setIconSize(icon_size)
        button.setFixedSize(button_size)
        return button

    def _icon(self, icon_path):
        icon = QIcon()
        icon.addFile(icon_path, QSize(), QIcon.Normal, QIcon.Off)
        return icon

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.actionOpen_Music.setText(QCoreApplication.translate("MainWindow", "Open Music", None))
        self.actionOpen_Playlist.setText(QCoreApplication.translate("MainWindow", "Open Playlist", None))
        self.labelSubtitle.setText(QCoreApplication.translate("MainWindow", "DESKTOP AUDIO CONTROLS", None))
        self.labelHeading.setText(QCoreApplication.translate("MainWindow", "Music Player", None))
        self.labelTimerCaption.setText(QCoreApplication.translate("MainWindow", "ELAPSED", None))
        self.labelTimer.setText(QCoreApplication.translate("MainWindow", "00:00:00", None))
        self.labelVolumeText.setText(QCoreApplication.translate("MainWindow", "VOLUME", None))
        self.toolButtonPlay.setText(QCoreApplication.translate("MainWindow", "...", None))
        self.toolButtonPause.setText(QCoreApplication.translate("MainWindow", "...", None))
        self.toolButtonStop.setText(QCoreApplication.translate("MainWindow", "...", None))
        self.toolButtonVolume.setText(QCoreApplication.translate("MainWindow", "...", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "File", None))
