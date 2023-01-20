import sys
import time
from PySide6.QtWidgets import *
from PySide6.QtCore import *


class Simple_timer_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.num = time.strftime("%X")

        vbox = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setText(str(self.num))
        vbox.addWidget(self.label)

        timer = QTimer(self)
        timer.timeout.connect(self.updateValue)
        timer.start(1000)

        self.setLayout(vbox)

        self.show()

    def updateValue(self):
        self.label.setText(time.strftime("%X"))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = Simple_timer_window()

    sys.exit(app.exec())
