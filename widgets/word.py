from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt

from util import Color

class Word(QWidget):
    def __init__(self, word):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        # self.setStyleSheet("""
        #     QWidget {

        #     }
        # """)

        self.word = word

        self.layout = QHBoxLayout()

        self.layout.addStretch()

        for v in word:
            if v != " ":
                self.layout.addWidget(Letter(v))
            else:
                widget = QWidget()
                widget.setFixedWidth(20)
                self.layout.addWidget(widget)

        self.layout.addStretch()

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
                
                color: %s;
                font: bold 20px;
            }
        """ % (Color.white, Color.dark_blue))

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFixedWidth(30)

    def show_letter(self):
        self.setText(self.letter)
    