import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import QSoundEffect


class Animation_area(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.frame_no = 0
        self.images = [
            QPixmap("images/frame-" + str(i+1) + ".png")
            for i in range(20)
        ]

        self.is_playing = True
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_value)
        self.timer.start(75)
        self.QSE = QSoundEffect()
        self.QSE.setSource(QUrl.fromLocalFile("sounds/rabbit_jump.wav"))

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.drawPixmap(QRect(0, 0, 320, 320), self.images[self.frame_no])
        p.end()

    def update_value(self):
        self.frame_no += 1
        if self.frame_no >= 20:
            self.frame_no = 0
            self.QSE.play()

        self.update()

    def toggle_play(self):
        if self.is_playing:
            self.timer.stop()
            self.is_playing = False
            return
        self.timer.start(75)
        self.is_playing = True

    def get_is_playing(self):
        return self.is_playing


class Simple_animation_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.anim_area = Animation_area()

        layout = QVBoxLayout()
        layout.addWidget(self.anim_area)

        self.pause_toggle_btn = QPushButton("Pause")
        self.pause_toggle_btn.clicked.connect(self.btn_callback)
        layout.addWidget(self.pause_toggle_btn)

        self.setLayout(layout)
        self.setMinimumSize(330, 400)

    def btn_callback(self):
        if self.anim_area.get_is_playing():
            self.pause_toggle_btn.setText("Play")
        else:
            self.pause_toggle_btn.setText("Pause")
        self.anim_area.toggle_play()


def main():
    app = QApplication(sys.argv)

    w = Simple_animation_window()
    w.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
