import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import QSoundEffect
from ui_physim import Ui_PhysicsSimulator


class PhysicsSimulator(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)

        self.ui = Ui_PhysicsSimulator()
        self.ui.setupUi(self)

        self.gravity = 10
        self.y_velocity = 4
        self.x_velocity = 12
        self.energy_loss = 3

        self.ui.gravity_slider.setValue(self.gravity)
        self.ui.y_velocity_slider.setValue(self.y_velocity)
        self.ui.x_velocity_slider.setValue(self.x_velocity)
        self.ui.energy_loss_slider.setValue(self.energy_loss)

        self.ui.gravity_slider.valueChanged.connect(self.gravity_changed)
        self.ui.y_velocity_slider.valueChanged.connect(self.y_velocity_changed)
        self.ui.x_velocity_slider.valueChanged.connect(self.x_velocity_changed)
        self.ui.energy_loss_slider.valueChanged.connect(
            self.energy_loss_changed)

        self.ui.start_button.clicked.connect(self.start)
        self.ui.stop_button.clicked.connect(self.stop)

        self.timer = QTimer()
        self.time = 0
        self.timer.timeout.connect(self.update_time)
        self.timer.timeout.connect(self.update)

        self.ball = Ball(self.gravity, self.y_velocity,
                         self.x_velocity, self.energy_loss)
        self.scene = QGraphicsScene()
        self.scene.addItem(self.ball)

        self.gravity_changed(self.gravity)
        self.y_velocity_changed(self.y_velocity)
        self.x_velocity_changed(self.x_velocity)
        self.energy_loss_changed(self.energy_loss)

        self.ui.graphicsView.setScene(self.scene)

    def gravity_changed(self, value: int) -> None:
        self.ui.gravity_label.setText(f"Gravity: {value} m/s^2")
        self.ball.gravity = value

    def y_velocity_changed(self, value: int) -> None:
        self.ui.y_velocity_label.setText(f"Y Velocity: {value} m/s")
        self.ball.y_velocity = value

    def x_velocity_changed(self, value: int) -> None:
        self.ui.x_velocity_label.setText(f"X Velocity: {value} m/s")
        self.ball.x_velocity = value

    def energy_loss_changed(self, value: int) -> None:
        self.ui.energy_lost_label.setText(f"Energy Loss: {value} %")
        self.ball.energy_loss = value

    def start(self) -> None:
        self.timer.start(10)

    def stop(self) -> None:
        self.timer.stop()

    def update(self) -> None:
        self.ball.update()
        self.ui.x_velocity_status.setText(
            f"X Velocity: {self.ball.x_velocity:.6f} m/s")
        self.ui.y_velocity_status.setText(
            f"Y Velocity: {self.ball.y_velocity:.6f} m/s")
        self.ui.energy_loss_status.setText(
            f"Energy Loss: {self.ball.energy_loss} %")
        self.ui.gravity_status.setText(
            f"Gravity: {self.ball.gravity:.6f} m/s^2")
        self.ui.speed_status.setText(
            f"Speed: {(self.ball.x_velocity ** 2 + self.ball.y_velocity ** 2) ** 0.5:.6f} m/s")

    def update_time(self) -> None:
        self.time += 0.01
        self.ui.time_status.setText(f"Time Elapsed: {self.time:.2f} s.")


class Ball(QGraphicsPixmapItem):
    def __init__(self, gravity: float = 0, y_velocity: float = 0, x_velocity: float = 0, energy_loss: float = 0) -> None:
        super().__init__()
        self.setPixmap(QPixmap("ball.png"))
        self.setPos(50, 50)
        self.setTransform(QTransform.fromScale(0.025, 0.025))
        self.gravity = gravity
        self.y_velocity = y_velocity
        self.x_velocity = x_velocity
        self.energy_loss = energy_loss
        self.sound = QSoundEffect()
        self.sound.setSource(QUrl.fromLocalFile("bounce.wav"))

    def update(self) -> None:
        self.x_velocity *= 1 - self.energy_loss / 1000
        self.y_velocity *= 1 - self.energy_loss / 1000
        self.y_velocity += self.gravity / 100
        self.setPos(self.x() + self.x_velocity, self.y() + self.y_velocity)
        if self.y() > 600 or self.y() < 50:
            self.y_velocity *= -1
            self.sound.play()
        if self.x() > 500 or self.x() < 50:
            self.x_velocity *= -1
            self.sound.play()
        if self.y() > 600:
            self.setPos(self.x(), 600)
        if self.y() < 50:
            self.setPos(self.x(), 50)
        if self.x() > 500:
            self.setPos(500, self.y())
        if self.x() < 50:
            self.setPos(50, self.y())


def main():
    app = QApplication(sys.argv)
    window = PhysicsSimulator()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
