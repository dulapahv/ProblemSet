# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'program3_3.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 500)
        self.geometry = QWidget(MainWindow)
        self.geometry.setObjectName(u"geometry")
        self.lineEdit = QLineEdit(self.geometry)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 381, 41))
        font = QFont()
        font.setPointSize(26)
        self.lineEdit.setFont(font)
        self.lineEdit.setReadOnly(True)
        self.gridLayoutWidget = QWidget(self.geometry)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 60, 381, 351))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_8 = QPushButton(self.gridLayoutWidget)
        self.btn_8.setObjectName(u"btn_8")
        font1 = QFont()
        font1.setPointSize(36)
        self.btn_8.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_8, 2, 1, 1, 1)

        self.btn_7 = QPushButton(self.gridLayoutWidget)
        self.btn_7.setObjectName(u"btn_7")
        self.btn_7.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_7, 2, 0, 1, 1)

        self.btn_5 = QPushButton(self.gridLayoutWidget)
        self.btn_5.setObjectName(u"btn_5")
        self.btn_5.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_5, 1, 1, 1, 1)

        self.btn_4 = QPushButton(self.gridLayoutWidget)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_4, 1, 0, 1, 1)

        self.btn_6 = QPushButton(self.gridLayoutWidget)
        self.btn_6.setObjectName(u"btn_6")
        self.btn_6.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_6, 1, 2, 1, 1)

        self.btn_3 = QPushButton(self.gridLayoutWidget)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_3, 0, 2, 1, 1)

        self.btn_9 = QPushButton(self.gridLayoutWidget)
        self.btn_9.setObjectName(u"btn_9")
        self.btn_9.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_9, 2, 2, 1, 1)

        self.btn_2 = QPushButton(self.gridLayoutWidget)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_2, 0, 1, 1, 1)

        self.btn_1 = QPushButton(self.gridLayoutWidget)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_1, 0, 0, 1, 1)

        self.btn_star = QPushButton(self.gridLayoutWidget)
        self.btn_star.setObjectName(u"btn_star")
        self.btn_star.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_star, 3, 0, 1, 1)

        self.btn_0 = QPushButton(self.gridLayoutWidget)
        self.btn_0.setObjectName(u"btn_0")
        self.btn_0.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_0, 3, 1, 1, 1)

        self.btn_square = QPushButton(self.gridLayoutWidget)
        self.btn_square.setObjectName(u"btn_square")
        self.btn_square.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_square, 3, 2, 1, 1)

        self.horizontalLayoutWidget = QWidget(self.geometry)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 420, 381, 74))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_talk = QPushButton(self.horizontalLayoutWidget)
        self.btn_talk.setObjectName(u"btn_talk")
        self.btn_talk.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_talk)

        self.btn_delete = QPushButton(self.horizontalLayoutWidget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_delete)

        MainWindow.setCentralWidget(self.geometry)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"KMITL Phone", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_star.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_square.setText(QCoreApplication.translate("MainWindow", u"#", None))
        self.btn_talk.setText(QCoreApplication.translate("MainWindow", u"Talk", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"<", None))
    # retranslateUi

