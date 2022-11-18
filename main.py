from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

from random import choice

from widgets import control, word
from util import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.keyboard = control.Control(self)

        with open('words.txt', 'r') as f:
            words = f.read().splitlines()
            self.current_word = word.Word(choice(words))
            print(words)

        self.setStyleSheet("""
            QMainWindow {
                background: %s;
            }
        """ % Color.blue)

        self.frame = QWidget()

        self.frame.layout = QVBoxLayout()
        self.frame.layout.addWidget(self.current_word)
        # add thing
        self.frame.layout.addStretch()
        self.frame.layout.addWidget(self.keyboard)
        self.frame.setLayout(self.frame.layout)

        self.setCentralWidget(self.frame)

    def clicked_event(self):
        button = self.sender()

        button.setStyleSheet("""
            QPushButton {
                background: #A65300;
                border-radius: 5px;

                color: %s;
                font: bold 20px;
            }
        """ % Color.white)

        button.setDisabled(True)

        self.keyboard.guesses.guesses.append(button.text())
        self.keyboard.guesses.update()

        # if button.text() in self.current_word.layout.children:
        #     for 

        for v in self.current_word.children():
            try:
                if v.letter == button.text():
                    v.show_letter()
            except AttributeError:
                continue


if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    window.show()

    print(window.size())

    app.exec()