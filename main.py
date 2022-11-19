from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QMessageBox
from PyQt6.QtGui import QPainter, QColor, QPixmap, QIcon, QImage
from PyQt6.QtCore import Qt, QRect, QTimer

from random import choice, randint
from time import sleep

from widgets import control, word, timer
from util import Color

import threading

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(1000,700)

        self.setStyleSheet("""
            QMainWindow {
                background: #9EDAFF;
            }
        """)

        self.sidebar = SideBar(self)
        self.timer = timer.Timer(self)

        self.timer_frame = QWidget()
        self.timer_frame.layout = QVBoxLayout()
        self.timer_frame.layout.addWidget(self.timer)
        self.timer_frame.layout.addStretch()
        self.timer_frame.setLayout(self.timer_frame.layout)

        self.frame = QWidget()

        self.frame.layout = QHBoxLayout()
        self.frame.layout.addWidget(self.sidebar)
        self.frame.layout.addStretch(1)
        self.frame.layout.addWidget(self.timer_frame)

        self.frame.layout.setContentsMargins(0,0,0,0)
        self.frame.setLayout(self.frame.layout)

        self.setCentralWidget(self.frame)


        self.ocean = QRect(0,200,1000,500)
        self.rov = QRect(550, 110, 320, 180)

        self.last = (1, 1)
        self.moving = True

        self.tick = QTimer(self)
        self.tick.timeout.connect(self.update)
        self.tick.start(300)

    def game_over(self, win):
        self.timer.timer.stop()

        for v in self.sidebar.controls.keys.children():
            try:
                v.setDisabled(True)
            except AttributeError as e:
                continue

        end_msg = QMessageBox()

        if win:
            end_msg.setIcon(QMessageBox.Icon.Information)
            end_msg.setText("You have successfully gotten revenge by messing up their run! They'll never touch your soldering iron again! Congratulations!")
        else:
            end_msg.setIcon(QMessageBox.Icon.Critical)
            end_msg.setText(f"You were caught and got shot {randint(2, 8)} times! Try again! The word was: {self.sidebar.current_word.word}")

        end_msg.exec()


    def lower_ocean(self):
        letters = set("".join(self.sidebar.current_word.word.split()))
        y_change = 480//len(letters)

        self.ocean.translate(0, y_change)

        if self.rov.y() + y_change > 550:
            self.rov.moveBottom(720)
            self.moving = False
            
            self.game_over(True)
        else: 
            self.rov.translate(0, y_change)
        

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)

        painter.fillRect(0,190,1000,10, QColor(Color.white))
        painter.fillRect(0,200,1000,500, QColor("#E0E0E0")) ##### 

        if self.moving:
            if self.last == (1,1):
                self.last = (1, -1)
            elif self.last == (1, -1):
                self.last = (-1, 1)
            elif self.last == (-1, 1):
                self.last = (-1, -1)
            else:
                self.last = (1,1)
        
            self.rov.translate(self.last[0]*3, self.last[1]*3)

        painter.drawPixmap(self.rov, QPixmap('assets/rov.png'))

        painter.setOpacity(0.5)

        painter.fillRect(self.ocean, QColor(Color.blue))

        painter.end()


class SideBar(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.parent = parent

        self.setStyleSheet("""
            QWidget {
                background: %s;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 10px;
            }
        """ % Color.dark_blue)

        with open('words.txt', 'r') as f:
            words = [v.rstrip() for v in f.readlines()]
            self.current_word = word.Word(choice(words))


        pixmap = QPixmap('assets/main.png')
        self.image = QLabel()
        
        self.image.setPixmap(pixmap)

        self.image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.controls = control.Control(self)
        

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.current_word)
        self.layout.addStretch()
        self.layout.addWidget(self.image)
        self.layout.addWidget(self.controls)

        self.setLayout(self.layout)

    def clicked_event(self):
        button = self.sender()
        button.setDisabled(True)

        count = 0
        for v in self.current_word.children():
            try:
                if v.letter == button.text():
                    v.show_letter()
                    count += 1
            except AttributeError as e:
                continue

        if count > 0:
            button.setStyleSheet("""
                QPushButton {
                    background: #00AD3D;
                    border-radius: 5px;

                    color: %s;
                    font: bold 20px;
                }
            """ % Color.white)

            self.parent.lower_ocean()
        else:
            button.setStyleSheet("""
                QPushButton {
                    background: #AD0000;
                    border-radius: 5px;

                    color: %s;
                    font: bold 20px;
                }
            """ % Color.white)

            self.controls.guesses.guesses.append(button.text())
            self.controls.guesses.update()



if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()