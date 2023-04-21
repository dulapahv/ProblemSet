# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Booking_List.ui'
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
from PySide6.QtWidgets import (QApplication, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Booking_List(object):
    def setupUi(self, Booking_List):
        if not Booking_List.objectName():
            Booking_List.setObjectName(u"Booking_List")
        Booking_List.resize(351, 305)
        self.centralwidget = QWidget(Booking_List)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.select_btn = QPushButton(self.centralwidget)
        self.select_btn.setObjectName(u"select_btn")

        self.verticalLayout.addWidget(self.select_btn)

        Booking_List.setCentralWidget(self.centralwidget)

        self.retranslateUi(Booking_List)

        QMetaObject.connectSlotsByName(Booking_List)
    # setupUi

    def retranslateUi(self, Booking_List):
        Booking_List.setWindowTitle(QCoreApplication.translate("Booking_List", u"Booking List", None))
        self.select_btn.setText(QCoreApplication.translate("Booking_List", u"Select Bookings ...", None))
    # retranslateUi

