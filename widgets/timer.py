from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtCore import QTimer

from util import Color


class Timer(QLabel):
    def __init__(self, parent):
        super().__init__("2:00")

        self.parent = parent

        self.setStyleSheet("""
            QLabel {
                background: %s;
                border-radius: 8px;
                padding: 10px;

                color: %s;
                font: bold 20px;
            }
        """ % (Color.dark_blue, Color.white))

        self.time = 120

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

    def update_timer(self):
        self.time -= 1

        self.setText(f"{self.time // 60}:{self.time % 60:02}")

        if self.time == 0:
            self.parent.game_over(False)
            return

        if self.time <= 30:
            self.setStyleSheet("""
                QLabel {
                    color: #AD0000;
                    font: bold 20px;
                }
            """)



