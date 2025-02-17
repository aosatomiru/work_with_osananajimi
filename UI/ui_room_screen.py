# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'room_screen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_RoomScreen(object):
    def setupUi(self, RoomScreen):
        if not RoomScreen.objectName():
            RoomScreen.setObjectName(u"RoomScreen")
        RoomScreen.resize(800, 600)
        self.centralwidget = QWidget(RoomScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.insideRoomLabel = QLabel(self.centralwidget)
        self.insideRoomLabel.setObjectName(u"insideRoomLabel")
        self.insideRoomLabel.setGeometry(QRect(0, 0, 800, 600))
        self.insideRoomLabel.setPixmap(QPixmap(u":/image/images/backgrounds/inside.jpg"))
        self.osanaText = QTextBrowser(self.centralwidget)
        self.osanaText.setObjectName(u"osanaText")
        self.osanaText.setGeometry(QRect(30, 470, 740, 105))
        self.osanaText.setStyleSheet(u"QTextBrowser {\n"
"	font: 75 16pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"}")
        self.osanaLabel = QLabel(self.centralwidget)
        self.osanaLabel.setObjectName(u"osanaLabel")
        self.osanaLabel.setGeometry(QRect(220, 40, 371, 471))
        self.osanaLabel.setPixmap(QPixmap(u":/image/images/character/figure1.png"))
        self.osanaLabel.setScaledContents(True)
        self.serifButton = QPushButton(self.centralwidget)
        self.serifButton.setObjectName(u"serifButton")
        self.serifButton.setGeometry(QRect(20, 410, 140, 45))
        self.serifButton.setStyleSheet(u"QPushButton{background: transparent;}")
        self.finishButton = QPushButton(self.centralwidget)
        self.finishButton.setObjectName(u"finishButton")
        self.finishButton.setGeometry(QRect(630, 410, 140, 45))
        self.finishButton.setStyleSheet(u"QPushButton{background: transparent;}")
        self.windowLabel = QLabel(self.centralwidget)
        self.windowLabel.setObjectName(u"windowLabel")
        self.windowLabel.setGeometry(QRect(20, 405, 760, 182))
        self.windowLabel.setStyleSheet(u"")
        self.windowLabel.setPixmap(QPixmap(u":/image/images/windows/textbox_serif.png"))
        self.windowLabel.setScaledContents(True)
        self.timerButton = QPushButton(self.centralwidget)
        self.timerButton.setObjectName(u"timerButton")
        self.timerButton.setGeometry(QRect(160, 410, 140, 45))
        self.timerButton.setStyleSheet(u"QPushButton{background: transparent;}")
        self.breakButton = QPushButton(self.centralwidget)
        self.breakButton.setObjectName(u"breakButton")
        self.breakButton.setGeometry(QRect(300, 410, 140, 45))
        self.breakButton.setStyleSheet(u"QPushButton{background: transparent;}")
        self.finishLabel = QLabel(self.centralwidget)
        self.finishLabel.setObjectName(u"finishLabel")
        self.finishLabel.setGeometry(QRect(630, 400, 140, 81))
        self.finishLabel.setPixmap(QPixmap(u":/image/images/windows/button_finish.png"))
        self.finishLabel.setScaledContents(True)
        RoomScreen.setCentralWidget(self.centralwidget)
        self.insideRoomLabel.raise_()
        self.osanaLabel.raise_()
        self.finishLabel.raise_()
        self.windowLabel.raise_()
        self.osanaText.raise_()
        self.timerButton.raise_()
        self.serifButton.raise_()
        self.finishButton.raise_()
        self.breakButton.raise_()

        self.retranslateUi(RoomScreen)

        QMetaObject.connectSlotsByName(RoomScreen)
    # setupUi

    def retranslateUi(self, RoomScreen):
        RoomScreen.setWindowTitle(QCoreApplication.translate("RoomScreen", u"MainWindow", None))
        self.insideRoomLabel.setText("")
        self.osanaText.setHtml(QCoreApplication.translate("RoomScreen", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u30e1\u30a4\u30ea\u30aa'; font-size:16pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u304a\u306f\u3088\u3046</p></body></html>", None))
        self.osanaLabel.setText("")
        self.serifButton.setText("")
        self.finishButton.setText("")
        self.windowLabel.setText("")
        self.timerButton.setText("")
        self.breakButton.setText("")
        self.finishLabel.setText("")
    # retranslateUi

