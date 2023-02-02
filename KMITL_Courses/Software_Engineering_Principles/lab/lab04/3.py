import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import QSoundEffect
import random


class Rabbit:
    def __init__(self):
        self.image = QPixmap("images/rabbit.png")
        self.x = 0
        self.y = 0
        self.w = 40
        self.h = 40

    def draw(self, p):
        p.drawPixmap(QRect(self.x, self.y, self.w, self.h), self.image)

    def random_pos(self, arena_w, arena_h):
        self.x = random.randint(0, arena_w - self.w)
        self.y = random.randint(0, arena_h - self.h)

    def is_hit(self, mouse_x, mouse_y):
        if (mouse_x < self.x + self.w and self.x < mouse_x) and (mouse_y > self.y and mouse_y < self.y + self.h):
            return True
        return False


class Animation_area(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setMinimumSize(300, 300)

        self.arena_w = 300
        self.arena_h = 300
        self.rabbit = Rabbit()

        timer = QTimer(self)
        timer.timeout.connect(self.update_value)
        timer.start(2000)

        self.QSH = QSoundEffect()
        self.QSH.setSource(QUrl.fromLocalFile("sounds/rabbit_hit.wav"))
        self.QSM = QSoundEffect()
        self.QSM.setSource(QUrl.fromLocalFile("sounds/rabbit_missed.wav"))

    def mousePressEvent(self, e):
        if self.rabbit.is_hit(e.pos().x(), e.pos().y()):
            self.QSH.play()
            print("Hit!!!")
        else:
            self.QSM.play()
            print("Miss")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        self.rabbit.draw(p)
        p.end()

    def update_value(self):
        self.rabbit.random_pos(self.arena_w, self.arena_h)
        self.update()


class Simple_animation_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.anim_area = Animation_area()

        layout = QVBoxLayout()
        layout.addWidget(self.anim_area)

        self.setLayout(layout)
        self.setMinimumSize(330, 400)


def main():
    app = QApplication(sys.argv)

    w = Simple_animation_window()
    w.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
