import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from program3_2 import Ui_Form


class TestUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.num = 0
        self.ui.inc_button.clicked.connect(self.inc_value)
        self.ui.dec_button.clicked.connect(self.dec_value)
        self.ui.reset_button.clicked.connect(self.reset_value)

    def inc_value(self):
        self.num += 1
        self.ui.num_label.setText(str(self.num))

    def dec_value(self):
        self.num -= 1
        self.ui.num_label.setText(str(self.num))

    def reset_value(self):
        self.num = 0
        self.ui.num_label.setText(str(self.num))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestUI()
    window.show()
    sys.exit(app.exec())
