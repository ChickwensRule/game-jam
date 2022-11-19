from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt

from util import Color


class Control(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.parent = parent

        self.setStyleSheet("""
            QWidget {
                background: %s;
                border-radius: 10px;
            }
        """ % Color.dark_blue)

        self.keys = Keyboard(self)
        
        self.guesses = Guesses()

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.keys)
        self.layout.addWidget(self.guesses)

        self.setLayout(self.layout)




class Keyboard(QWidget):
    def __init__(self, parent):
        super().__init__() 

        self.parent = parent

        self.layout = QGridLayout()

        for i in range(2):
            for i2 in range(13):
                button = Button(chr((13*i)+i2+65))
                self.layout.addWidget(button, i, i2)

                button.clicked.connect(self.parent.parent.clicked_event)

        self.layout.setSpacing(5)
        self.setLayout(self.layout)

    # def clicked_event(self, button):
    #     button = self.sender()

    #     button.setStyleSheet("""
    #         QPushButton {
    #             background: #A65300;
    #             border-radius: 5px;

    #             color: %s;
    #             font: bold 20px;
    #         }
    #     """ % Color.white)

    #     button.setDisabled(True)

    #     self.parent.guesses.guesses.append(button.text())
    #     self.parent.guesses.update()

class Guesses(QLabel):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            QLabel {
                background: %s;
                padding: 10px;

                color: %s;
                font: bold 15px;
            }
        """ % (Color.white, Color.dark_blue))
        
        self.setWordWrap(True)

        self.guesses = []

    def update(self):
        self.setText(f"{', '.join(self.guesses)} ({len(self.guesses)}/5)")

    

class Button(QPushButton):
    def __init__(self, text):
        super().__init__(text)

        self.setStyleSheet("""
            QPushButton {
                background: %s;
                border-radius: 5px;

                color: %s;
                font: bold 20px;
            }

            QPushButton:hover {
                background: #E38F3B;
            }
        """ % (Color.orange, Color.white))

        self.setFixedSize(25, 25)
        # self.clicked.connect(self.clicked_event)



    # def key_pressed(self):

