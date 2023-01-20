import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    btn = QPushButton('Button', w)
    btn.move(50, 50)
    w.show()
    sys.exit(app.exec())
