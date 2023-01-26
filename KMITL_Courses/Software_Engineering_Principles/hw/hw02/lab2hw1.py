import sys
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton,
                               QLabel, QVBoxLayout, QGridLayout, QLineEdit, QDialog, QSpinBox)
from PySide6.QtCore import Qt


class Matrix_to_latex(QWidget):
    def __init__(self) -> None:
        QWidget.__init__(self, None)
        vbox = QVBoxLayout()
        self.header = QLabel(self)
        self.header.setText("Matrix to LaTeX Converter")
        self.header.setStyleSheet(
            "font-weight: bold; font-size: 32px; font-family: Arial; letter-spacing: 1px; color: #ffffff;")
        vbox.addWidget(self.header)
        self.header.setAlignment(Qt.AlignCenter)

        self.label = QLabel(self)
        self.label.setText("Set the matrix dimensions")
        vbox.addWidget(self.label)

        self.row_label = QLabel(self)
        self.row_label.setText("Rows")
        vbox.addWidget(self.row_label)

        self.row_spin = QSpinBox(self)
        self.row_spin.setRange(1, 10)
        self.row_spin.setValue(1)

        vbox.addWidget(self.row_spin)

        self.column_label = QLabel(self)
        self.column_label.setText("Columns")
        vbox.addWidget(self.column_label)

        self.column_spin = QSpinBox(self)
        self.column_spin.setRange(1, 10)
        self.column_spin.setValue(1)
        vbox.addWidget(self.column_spin)

        self.next_button = QPushButton('Enter Matrix Value', self)
        self.next_button.clicked.connect(self.showGrid)
        vbox.addWidget(self.next_button)

        self.setLayout(vbox)

        self.resize(500, 300)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), "#282c34")
        self.setPalette(p)

        self.next_button.setStyleSheet("QPushButton { font-size: 20px; font-family: Arial; letter-spacing: 1px; background-color: #fa971a; color: #ffffff; border: 1px solid #fa971a; border-radius: 10px; padding: 5px; } QPushButton:pressed { font-size: 20px; font-family: Arial; letter-spacing: 1px; background-color: #ffac28; color: #ffffff; border: 1px solid #ffac28; border-radius: 10px; padding: 5px;} ")
        self.setStyleSheet(
            "QLabel { color: #ffffff; font-size: 20px; font-family: Arial; letter-spacing: 1px;}")

        self.row_spin.setStyleSheet(
            "font-size: 20px; font-family: Arial; letter-spacing: 1px; background-color: #626c80; color: #ffffff; border: 1px solid #626c80; border-radius: 5px; padding: 5px;")
        self.column_spin.setStyleSheet(
            "font-size: 20px; font-family: Arial; letter-spacing: 1px; background-color: #626c80; color: #ffffff; border: 1px solid #626c80; border-radius: 5px; padding: 5px;")

        self.show()

    def showGrid(self) -> None:
        dialog = QDialog(self)
        grid = QGridLayout()
        self.entries = []

        for row in range(self.row_spin.value()):
            for col in range(self.column_spin.value()):
                self.entries.append(QLineEdit(self))
                self.entries[-1].setText("0")
                grid.addWidget(self.entries[-1], row, col)
                self.entries[-1].setStyleSheet(
                    "font-size: 20px; font-family: Arial; letter-spacing: 1px; background-color: #626c80; color: #ffffff; border: 1px solid #626c80; border-radius: 5px; padding: 5px;")

        self.entries[0].setFocus()
        self.convert_button = QPushButton('Convert to LaTeX', self)
        self.convert_button.clicked.connect(self.result_dialog)
        self.convert_button.clicked.connect(dialog.close)
        grid.addWidget(self.convert_button, self.row_spin.value() +
                       1, 0, 1, self.column_spin.value())
        dialog.setLayout(grid)

        self.setAutoFillBackground(True)

        p = dialog.palette()
        p.setColor(dialog.backgroundRole(), "#282c34")
        dialog.setPalette(p)

        self.convert_button.setStyleSheet(
            "QPushButton { font-size: 20px; font-family: Arial; letter-spacing: 1px; background-color: #fa971a; color: #ffffff; border: 1px solid #fa971a; border-radius: 10px; padding: 5px; } QPushButton:pressed { font-size: 20px; font-family: Arial; letter-spacing: 1px; background-color: #ffac28; color: #ffffff; border: 1px solid #ffac28; border-radius: 10px; padding: 5px;} ")

        self.setStyleSheet(
            "QLabel { color: #ffffff; font-size: 20px; font-family: Arial; letter-spacing: 1px;}")

        dialog.show()

    def result_dialog(self) -> None:
        dialog = QDialog(self)
        layout = QVBoxLayout()

        ans = QLabel(dialog)
        ans.setText(self.matrix_to_latex())
        ans.setTextInteractionFlags(Qt.TextSelectableByMouse)
        dialog.setFixedWidth(768)
        layout.addWidget(ans)

        copy_button = QPushButton("Copy to clipboard", self)
        copy_button.clicked.connect(lambda: QApplication.clipboard().setText(
            self.matrix_to_latex()))
        layout.addWidget(copy_button)

        close_button = QPushButton("Close window", self)
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        dialog.setLayout(layout)

        self.setAutoFillBackground(True)

        p = dialog.palette()
        p.setColor(dialog.backgroundRole(), "#282c34")
        dialog.setPalette(p)

        copy_button.setStyleSheet(
            "QPushButton { font-size: 20px; font-family: Arial; letter-spacing: 1px; background-color: #fa971a; color: #ffffff; border: 1px solid #fa971a; border-radius: 10px; padding: 5px; } QPushButton:pressed { font-size: 20px; font-family: Arial; letter-spacing: 1px; background-color: #ffac28; color: #ffffff; border: 1px solid #ffac28; border-radius: 10px; padding: 5px;} ")

        close_button.setStyleSheet(
            "QPushButton { font-size: 20px; font-family: Arial; letter-spacing: 1px; background-color: #fa971a; color: #ffffff; border: 1px solid #fa971a; border-radius: 10px; padding: 5px; } QPushButton:pressed { font-size: 20px; font-family: Arial; letter-spacing: 1px; background-color: #ffac28; color: #ffffff; border: 1px solid #ffac28; border-radius: 10px; padding: 5px;} ")

        self.setStyleSheet(
            "QLabel { color: #ffffff; font-size: 20px; font-family: Arial; letter-spacing: 1px;}")

        ans.setStyleSheet(
            "font-size: 20px; font-family: Arial; letter-spacing: 1px; background-color: #626c80; color: #ffffff; border: 1px solid #626c80; border-radius: 5px; padding: 5px;")

        dialog.show()

    def matrix_to_latex(self) -> str:
        latex = "\\begin{bmatrix}\n"
        for row in range(self.row_spin.value()):
            for col in range(self.column_spin.value()):
                latex += self.entries[row *
                                      self.column_spin.value() + col].text()
                if col != self.column_spin.value() - 1:
                    latex += " & "
            if row != self.row_spin.value() - 1:
                latex += " \\\\"
            latex += "\n"
        latex += "\\end{bmatrix}"
        return latex


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Matrix_to_latex()
    app.setApplicationName("Matrix to LaTeX Converter")
    sys.exit(app.exec())
