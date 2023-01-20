import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *


class Currency_converter(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        vbox = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setText(
            "Enter the amount of money to convert from:")
        vbox.addWidget(self.label)
        self.usd_to_thb_rate = 0.033
        self.thb_to_usd_rate = 30.0

        self.input = QLineEdit(self)
        vbox.addWidget(self.input)

        thb_to_usd = QPushButton('THB -> USD', self)
        thb_to_usd.clicked.connect(self.thb_to_usd)
        vbox.addWidget(thb_to_usd)

        usd_to_thb = QPushButton('USD -> THB', self)
        usd_to_thb.clicked.connect(self.usd_to_thb)
        vbox.addWidget(usd_to_thb)

        self.setLayout(vbox)

        self.show()

    def thb_to_usd(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()

        label = QLabel(dialog)
        try:
            label.setText(
                f"Converted amount: {str(round(float(self.input.text()) * self.usd_to_thb_rate, 3))} USD")
        except:
            label.setText("Please enter a number")
        layout.addWidget(label)

        close_button = QPushButton("Close window", self)
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        dialog.setLayout(layout)

        dialog.show()

    def usd_to_thb(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()

        label = QLabel(dialog)
        try:
            label.setText(
                f"Converted amount: {str(round(float(self.input.text()) * self.thb_to_usd_rate, 3))} THB")
        except:
            label.setText("Please enter a number")
        layout.addWidget(label)

        close_button = QPushButton("Close window", self)
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        dialog.setLayout(layout)

        dialog.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = Currency_converter()

    sys.exit(app.exec())
