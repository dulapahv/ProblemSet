# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Notepad.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Notepad(object):
    def setupUi(self, Notepad):
        if not Notepad.objectName():
            Notepad.setObjectName(u"Notepad")
        Notepad.resize(800, 641)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Notepad.sizePolicy().hasHeightForWidth())
        Notepad.setSizePolicy(sizePolicy)
        self.actionNew = QAction(Notepad)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(Notepad)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(Notepad)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(Notepad)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionExit = QAction(Notepad)
        self.actionExit.setObjectName(u"actionExit")
        self.actionCut = QAction(Notepad)
        self.actionCut.setObjectName(u"actionCut")
        self.actionCopy = QAction(Notepad)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPaste = QAction(Notepad)
        self.actionPaste.setObjectName(u"actionPaste")
        self.actionSelect_all = QAction(Notepad)
        self.actionSelect_all.setObjectName(u"actionSelect_all")
        self.actionZoom_in = QAction(Notepad)
        self.actionZoom_in.setObjectName(u"actionZoom_in")
        self.actionZoom_out = QAction(Notepad)
        self.actionZoom_out.setObjectName(u"actionZoom_out")
        self.actionDefault_zoom = QAction(Notepad)
        self.actionDefault_zoom.setObjectName(u"actionDefault_zoom")
        self.centralwidget = QWidget(Notepad)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        font = QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setFrameShape(QFrame.NoFrame)
        self.plainTextEdit.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, -1, -1, -1)
        self.label_line_col = QLabel(self.centralwidget)
        self.label_line_col.setObjectName(u"label_line_col")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_line_col.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_line_col)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setEnabled(False)
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.VLine)

        self.horizontalLayout_3.addWidget(self.line)

        self.label_word_count = QLabel(self.centralwidget)
        self.label_word_count.setObjectName(u"label_word_count")
        self.label_word_count.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_word_count)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setEnabled(False)
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setFrameShape(QFrame.VLine)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.label_char_count = QLabel(self.centralwidget)
        self.label_char_count.setObjectName(u"label_char_count")
        self.label_char_count.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_char_count)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setEnabled(False)
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setFrameShape(QFrame.VLine)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.label_zoom = QLabel(self.centralwidget)
        self.label_zoom.setObjectName(u"label_zoom")
        self.label_zoom.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_zoom)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        Notepad.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Notepad)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        Notepad.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelect_all)
        self.menuView.addAction(self.actionZoom_in)
        self.menuView.addAction(self.actionZoom_out)
        self.menuView.addAction(self.actionDefault_zoom)

        self.retranslateUi(Notepad)

        QMetaObject.connectSlotsByName(Notepad)
    # setupUi

    def retranslateUi(self, Notepad):
        Notepad.setWindowTitle(QCoreApplication.translate("Notepad", u"Untitled - Notepad", None))
        self.actionNew.setText(QCoreApplication.translate("Notepad", u"New", None))
        self.actionOpen.setText(QCoreApplication.translate("Notepad", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("Notepad", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate("Notepad", u"Save as", None))
        self.actionExit.setText(QCoreApplication.translate("Notepad", u"Exit", None))
        self.actionCut.setText(QCoreApplication.translate("Notepad", u"Cut", None))
        self.actionCopy.setText(QCoreApplication.translate("Notepad", u"Copy", None))
        self.actionPaste.setText(QCoreApplication.translate("Notepad", u"Paste", None))
        self.actionSelect_all.setText(QCoreApplication.translate("Notepad", u"Select all", None))
        self.actionZoom_in.setText(QCoreApplication.translate("Notepad", u"Zoom in", None))
        self.actionZoom_out.setText(QCoreApplication.translate("Notepad", u"Zoom out", None))
        self.actionDefault_zoom.setText(QCoreApplication.translate("Notepad", u"Default zoom", None))
        self.plainTextEdit.setPlainText("")
        self.label_line_col.setText(QCoreApplication.translate("Notepad", u"Ln 1, Col 1", None))
        self.label_word_count.setText(QCoreApplication.translate("Notepad", u"Word: 0", None))
        self.label_char_count.setText(QCoreApplication.translate("Notepad", u"Character: 0", None))
        self.label_zoom.setText(QCoreApplication.translate("Notepad", u"100%", None))
        self.menuFile.setTitle(QCoreApplication.translate("Notepad", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("Notepad", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("Notepad", u"View", None))
    # retranslateUi

