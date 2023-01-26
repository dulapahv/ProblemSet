import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from program3_3 import Ui_MainWindow


class KMITLPhone(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_1.clicked.connect(lambda: self.add_text("1"))
        self.ui.btn_2.clicked.connect(lambda: self.add_text("2"))
        self.ui.btn_3.clicked.connect(lambda: self.add_text("3"))
        self.ui.btn_4.clicked.connect(lambda: self.add_text("4"))
        self.ui.btn_5.clicked.connect(lambda: self.add_text("5"))
        self.ui.btn_6.clicked.connect(lambda: self.add_text("6"))
        self.ui.btn_7.clicked.connect(lambda: self.add_text("7"))
        self.ui.btn_8.clicked.connect(lambda: self.add_text("8"))
        self.ui.btn_9.clicked.connect(lambda: self.add_text("9"))
        self.ui.btn_0.clicked.connect(lambda: self.add_text("0"))
        self.ui.btn_star.clicked.connect(lambda: self.add_text("*"))
        self.ui.btn_square.clicked.connect(lambda: self.add_text("#"))
        self.ui.btn_delete.clicked.connect(self.delete)
        self.ui.btn_talk.clicked.connect(self.talk)

    def add_text(self, text):
        self.ui.lineEdit.setText(self.ui.lineEdit.text() + text)

    def delete(self):
        self.ui.lineEdit.setText(self.ui.lineEdit.text()[:-1])

    def talk(self):
        msg = QMessageBox()
        msg.setText(f"Dialing <<{self.ui.lineEdit.text()}>>")
        msg.setWindowTitle("Dialing")
        msg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KMITLPhone()
    window.show()
    sys.exit(app.exec())
