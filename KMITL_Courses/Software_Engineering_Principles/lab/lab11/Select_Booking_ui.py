# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Select_Booking.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Select_Booking(object):
    def setupUi(self, Select_Booking):
        if not Select_Booking.objectName():
            Select_Booking.setObjectName(u"Select_Booking")
        Select_Booking.resize(278, 127)
        self.centralwidget = QWidget(Select_Booking)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.day = QLineEdit(self.centralwidget)
        self.day.setObjectName(u"day")

        self.verticalLayout_3.addWidget(self.day)

        self.month = QLineEdit(self.centralwidget)
        self.month.setObjectName(u"month")

        self.verticalLayout_3.addWidget(self.month)

        self.year = QLineEdit(self.centralwidget)
        self.year.setObjectName(u"year")

        self.verticalLayout_3.addWidget(self.year)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.submit_btn = QPushButton(self.centralwidget)
        self.submit_btn.setObjectName(u"submit_btn")

        self.verticalLayout.addWidget(self.submit_btn)

        Select_Booking.setCentralWidget(self.centralwidget)

        self.retranslateUi(Select_Booking)

        QMetaObject.connectSlotsByName(Select_Booking)
    # setupUi

    def retranslateUi(self, Select_Booking):
        Select_Booking.setWindowTitle(QCoreApplication.translate("Select_Booking", u"Select Booking", None))
        self.label.setText(QCoreApplication.translate("Select_Booking", u"Day", None))
        self.label_2.setText(QCoreApplication.translate("Select_Booking", u"Month", None))
        self.label_3.setText(QCoreApplication.translate("Select_Booking", u"Year", None))
        self.submit_btn.setText(QCoreApplication.translate("Select_Booking", u"Submit", None))
    # retranslateUi

