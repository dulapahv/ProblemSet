# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'physim.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_PhysicsSimulator(object):
    def setupUi(self, PhysicsSimulator):
        if not PhysicsSimulator.objectName():
            PhysicsSimulator.setObjectName(u"PhysicsSimulator")
        PhysicsSimulator.resize(800, 600)
        self.centralwidget = QWidget(PhysicsSimulator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 801, 601))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 0, 6)
        self.status_label = QLabel(self.horizontalLayoutWidget)
        self.status_label.setObjectName(u"status_label")
        font = QFont()
        font.setPointSize(14)
        self.status_label.setFont(font)

        self.verticalLayout.addWidget(self.status_label)

        self.time_status = QLabel(self.horizontalLayoutWidget)
        self.time_status.setObjectName(u"time_status")
        font1 = QFont()
        font1.setPointSize(12)
        self.time_status.setFont(font1)

        self.verticalLayout.addWidget(self.time_status)

        self.gravity_status = QLabel(self.horizontalLayoutWidget)
        self.gravity_status.setObjectName(u"gravity_status")
        self.gravity_status.setFont(font1)

        self.verticalLayout.addWidget(self.gravity_status)

        self.y_velocity_status = QLabel(self.horizontalLayoutWidget)
        self.y_velocity_status.setObjectName(u"y_velocity_status")
        self.y_velocity_status.setFont(font1)

        self.verticalLayout.addWidget(self.y_velocity_status)

        self.x_velocity_status = QLabel(self.horizontalLayoutWidget)
        self.x_velocity_status.setObjectName(u"x_velocity_status")
        self.x_velocity_status.setFont(font1)

        self.verticalLayout.addWidget(self.x_velocity_status)

        self.energy_loss_status = QLabel(self.horizontalLayoutWidget)
        self.energy_loss_status.setObjectName(u"energy_loss_status")
        self.energy_loss_status.setFont(font1)

        self.verticalLayout.addWidget(self.energy_loss_status)

        self.speed_status = QLabel(self.horizontalLayoutWidget)
        self.speed_status.setObjectName(u"speed_status")
        self.speed_status.setFont(font1)

        self.verticalLayout.addWidget(self.speed_status)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.gravity_label = QLabel(self.horizontalLayoutWidget)
        self.gravity_label.setObjectName(u"gravity_label")
        self.gravity_label.setFont(font1)

        self.verticalLayout.addWidget(self.gravity_label)

        self.gravity_slider = QSlider(self.horizontalLayoutWidget)
        self.gravity_slider.setObjectName(u"gravity_slider")
        self.gravity_slider.setMinimum(-100)
        self.gravity_slider.setMaximum(100)
        self.gravity_slider.setOrientation(Qt.Horizontal)
        self.gravity_slider.setTickPosition(QSlider.TicksBelow)

        self.verticalLayout.addWidget(self.gravity_slider)

        self.y_velocity_label = QLabel(self.horizontalLayoutWidget)
        self.y_velocity_label.setObjectName(u"y_velocity_label")
        self.y_velocity_label.setFont(font1)

        self.verticalLayout.addWidget(self.y_velocity_label)

        self.y_velocity_slider = QSlider(self.horizontalLayoutWidget)
        self.y_velocity_slider.setObjectName(u"y_velocity_slider")
        self.y_velocity_slider.setMinimum(-100)
        self.y_velocity_slider.setMaximum(100)
        self.y_velocity_slider.setOrientation(Qt.Horizontal)
        self.y_velocity_slider.setTickPosition(QSlider.TicksBelow)

        self.verticalLayout.addWidget(self.y_velocity_slider)

        self.x_velocity_label = QLabel(self.horizontalLayoutWidget)
        self.x_velocity_label.setObjectName(u"x_velocity_label")
        self.x_velocity_label.setFont(font1)

        self.verticalLayout.addWidget(self.x_velocity_label)

        self.x_velocity_slider = QSlider(self.horizontalLayoutWidget)
        self.x_velocity_slider.setObjectName(u"x_velocity_slider")
        self.x_velocity_slider.setMinimum(-100)
        self.x_velocity_slider.setMaximum(100)
        self.x_velocity_slider.setOrientation(Qt.Horizontal)
        self.x_velocity_slider.setTickPosition(QSlider.TicksBelow)

        self.verticalLayout.addWidget(self.x_velocity_slider)

        self.energy_lost_label = QLabel(self.horizontalLayoutWidget)
        self.energy_lost_label.setObjectName(u"energy_lost_label")
        self.energy_lost_label.setFont(font1)

        self.verticalLayout.addWidget(self.energy_lost_label)

        self.energy_loss_slider = QSlider(self.horizontalLayoutWidget)
        self.energy_loss_slider.setObjectName(u"energy_loss_slider")
        self.energy_loss_slider.setMinimum(-20)
        self.energy_loss_slider.setMaximum(20)
        self.energy_loss_slider.setOrientation(Qt.Horizontal)
        self.energy_loss_slider.setInvertedControls(False)
        self.energy_loss_slider.setTickPosition(QSlider.TicksBelow)

        self.verticalLayout.addWidget(self.energy_loss_slider)

        self.start_button = QPushButton(self.horizontalLayoutWidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setFont(font)

        self.verticalLayout.addWidget(self.start_button)

        self.stop_button = QPushButton(self.horizontalLayoutWidget)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setFont(font)

        self.verticalLayout.addWidget(self.stop_button)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.graphicsView = QGraphicsView(self.horizontalLayoutWidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(500, 0))
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout.addWidget(self.graphicsView)

        PhysicsSimulator.setCentralWidget(self.centralwidget)

        self.retranslateUi(PhysicsSimulator)

        QMetaObject.connectSlotsByName(PhysicsSimulator)
    # setupUi

    def retranslateUi(self, PhysicsSimulator):
        PhysicsSimulator.setWindowTitle(QCoreApplication.translate("PhysicsSimulator", u"PhysicsSimulator", None))
        self.status_label.setText(QCoreApplication.translate("PhysicsSimulator", u"Status", None))
        self.time_status.setText(QCoreApplication.translate("PhysicsSimulator", u"Time Elapsed: 0.00 s.", None))
        self.gravity_status.setText(QCoreApplication.translate("PhysicsSimulator", u"Gravity: 0.000000 m/s^2", None))
        self.y_velocity_status.setText(QCoreApplication.translate("PhysicsSimulator", u"Y Velocity: 0.000000 m/s", None))
        self.x_velocity_status.setText(QCoreApplication.translate("PhysicsSimulator", u"X Velocity: 0.000000 m/s", None))
        self.energy_loss_status.setText(QCoreApplication.translate("PhysicsSimulator", u"Energy Loss: 0 %", None))
        self.speed_status.setText(QCoreApplication.translate("PhysicsSimulator", u"Speed: 0.000000 m/s", None))
        self.gravity_label.setText(QCoreApplication.translate("PhysicsSimulator", u"Gravity", None))
        self.y_velocity_label.setText(QCoreApplication.translate("PhysicsSimulator", u"Y Velocity", None))
        self.x_velocity_label.setText(QCoreApplication.translate("PhysicsSimulator", u"X Velocity", None))
        self.energy_lost_label.setText(QCoreApplication.translate("PhysicsSimulator", u"Energy Loss", None))
        self.start_button.setText(QCoreApplication.translate("PhysicsSimulator", u"Start", None))
        self.stop_button.setText(QCoreApplication.translate("PhysicsSimulator", u"Stop", None))
    # retranslateUi

