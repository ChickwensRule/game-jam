from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt

from util import Color

class Word(QWidget):
    def __init__(self, word):
        super().__init__()

        self.word = word

        self.layout = QHBoxLayout()

        for v in word:
            if v != " ":
                self.layout.addWidget(Letter(v))
            else:
                widget = QWidget()
                widget.setFixedWidth(20)
                self.layout.addWidget(widget)

        self.setLayout(self.layout)
        

class Letter(QLabel):
    def __init__(self, letter):
        super().__init__()

        self.letter = letter

        self.setStyleSheet("""
            QLabel {
                background: %s;
                padding: 8px;
                border-radius: 8px;

                font: bold 20px;
            }
        """ % Color.white)

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFixedWidth(30)

    def show_letter(self):
        self.setText(self.letter)
    