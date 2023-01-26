import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QMessageBox)
from ui_Notepad import Ui_Notepad


class Notepad(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)

        self.ui = Ui_Notepad()
        self.ui.setupUi(self)

        self.ui.actionNew.triggered.connect(self.new)
        self.ui.actionOpen.triggered.connect(self.open)
        self.ui.actionSave.triggered.connect(self.save)
        self.ui.actionExit.triggered.connect(self.close)

        self.ui.actionCut.triggered.connect(self.cut)
        self.ui.actionCopy.triggered.connect(self.copy)
        self.ui.actionPaste.triggered.connect(self.paste)
        self.ui.actionSelect_all.triggered.connect(self.select_all)

        self.ui.actionZoom_in.triggered.connect(self.zoom_in)
        self.ui.actionZoom_out.triggered.connect(self.zoom_out)
        self.ui.actionDefault_zoom.triggered.connect(self.default_zoom)
        self.default_font_size = self.ui.plainTextEdit.font().pointSize()
        self.zoom_percent = 100
        self.ui.label_zoom.setText(f"{self.zoom_percent}%")

        self.ui.plainTextEdit.cursorPositionChanged.connect(self.line_col)
        self.ui.plainTextEdit.textChanged.connect(self.count_word)
        self.ui.plainTextEdit.textChanged.connect(self.count_char)

        self.is_saved = True

    def new(self):
        if self.ui.plainTextEdit.toPlainText() and not self.is_saved:
            self.save()
        self.ui.plainTextEdit.setPlainText("")
        self.setWindowTitle("Untitled - Notepad")

    def open(self):
        if self.ui.plainTextEdit.toPlainText() and not self.is_saved:
            self.save()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "Text Files (*.txt)")
        if file_name:
            try:
                with open(file_name, "rb") as f:
                    text = f.read().decode("utf-8")
                    self.ui.plainTextEdit.setPlainText(text)
            except Exception as e:
                QMessageBox.warning(
                    self, "Error", f"Failed to read file: {e}")
            self.is_saved = True
            self.setWindowTitle(self.windowTitle()[1:])
            self.setWindowTitle(f"{file_name} - Notepad")

    def save(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "Text Files (*.txt)")
        if file_name:
            try:
                with open(file_name, "wb") as f:
                    text = self.ui.plainTextEdit.toPlainText()
                    f.write(text.encode("utf-8"))
            except Exception as e:
                QMessageBox.warning(
                    self, "Warning", f"Cannot save file: {e}")
            self.is_saved = True
            self.setWindowTitle(self.windowTitle()[1:])
            self.setWindowTitle(f"{file_name} - Notepad")

    def close(self):
        if self.ui.plainTextEdit.toPlainText() and not self.is_saved:
            self.save()
        exit(0)

    def cut(self):
        self.copy()
        self.ui.plainTextEdit.textCursor().removeSelectedText()

    def copy(self):
        QApplication.clipboard().setText(self.ui.plainTextEdit.textCursor().selectedText())

    def paste(self):
        self.ui.plainTextEdit.insertPlainText(QApplication.clipboard().text())

    def select_all(self):
        self.ui.plainTextEdit.selectAll()

    def zoom_in(self):
        if self.zoom_percent + 10 > 500:
            return
        font = self.ui.plainTextEdit.font()
        font.setPointSize(font.pointSize() + 1)
        self.ui.plainTextEdit.setFont(font)
        self.zoom_percent += 10
        self.ui.label_zoom.setText(str(f"{self.zoom_percent}%"))

    def zoom_out(self):
        if self.zoom_percent - 10 < 10:
            return
        font = self.ui.plainTextEdit.font()
        font.setPointSize(font.pointSize() - 1)
        self.ui.plainTextEdit.setFont(font)
        self.zoom_percent -= 10
        self.ui.label_zoom.setText(str(f"{self.zoom_percent}%"))

    def default_zoom(self):
        font = self.ui.plainTextEdit.font()
        font.setPointSize(self.default_font_size)
        self.ui.plainTextEdit.setFont(font)
        self.zoom_percent = 100
        self.ui.label_zoom.setText(str(f"{self.zoom_percent}%"))

    def line_col(self):
        line = self.ui.plainTextEdit.textCursor().blockNumber() + 1
        col = self.ui.plainTextEdit.textCursor().columnNumber() + 1
        self.ui.label_line_col.setText(str(f"Ln {line:,}, Col {col:,}"))

    def count_word(self):
        text = self.ui.plainTextEdit.toPlainText()
        self.ui.label_word_count.setText(str(f"Word: {len(text.split()):,}"))

    def count_char(self):
        if self.is_saved:
            self.is_saved = False
            self.setWindowTitle(f"*{self.windowTitle()}")
        text = self.ui.plainTextEdit.toPlainText()
        self.ui.label_char_count.setText(str(f"Character: {len(text):,}"))

    def closeEvent(self, event):
        if self.ui.plainTextEdit.toPlainText() and not self.is_saved:
            self.save()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Notepad()
    window.show()
    sys.exit(app.exec())
