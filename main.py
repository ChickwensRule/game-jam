from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtGui import QPainter, QColor, QImage
from PyQt6.QtCore import Qt, QRect, QTimer

from random import choice, randint
from time import sleep

from widgets import control, word
from util import Color

import threading


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(1000,700)

        self.setStyleSheet("""
            QMainWindow {
                background: #9EDAFF;
            }
        """)

        self.sidebar = SideBar()

        self.frame = QWidget()

        self.frame.layout = QHBoxLayout()
        self.frame.layout.addWidget(self.sidebar)
        self.frame.layout.addWidget(QWidget(), 2000)

        self.frame.layout.setContentsMargins(0,0,0,0)
        self.frame.setLayout(self.frame.layout)

        self.setCentralWidget(self.frame)


        self.ocean = QRect(0,200,1000,500)
        self.rov = QRect(600, 700-550, 480, 270)

        self.last = (1, 1)
        # 1, 1: 1, -1: -1, 1: -1, -1

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(300)
            # self.update()
            # sleep(1)

        self.lower_ocean()

    def lower_ocean(self):
        self.ocean.translate(0,200)

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)

        if self.last == (1,1):
            self.last = (1, -1)
        elif self.last == (1, -1):
            self.last = (-1, 1)
        elif self.last == (-1, 1):
            self.last = (-1, -1)
        else:
            self.last = (1,1)
        
        self.rov.translate(self.last[0]*2, self.last[1]*2)

        self.rov.translate(0, 1)

        painter.drawImage(self.rov, QImage('assets/rov2.png'))
        # self.rov.move

        # self.rov.translate(100, 100)

        # t = threading.Thread(target=lambda x: self.move_rov(painter))
        # t.start()


        # timer = QTimer(self)
        # timer.timeout.connect(lambda: self.move_rov(painter))
        # timer.start(1000)

        # self.move_rov()



        painter.setOpacity(0.5)

        # self.ocean = QRect(0,200,1000,500)

        self.ocean.translate(0, 1)

        painter.fillRect(self.ocean, QColor(Color.blue))

        # self.ocean.tra

        painter.end()
        # self.drawBezierCurve(qp)
        # qp.end()

    # def move_rov(self, painter):
    # #     # # while True:
    #     # self.rotation += 5
    # #     #     # self.rov = self.rov.transformed(QTransform().rotate(self.rotation))

    # #     #     # painter.drawPixmap(600, 700-500, int(self.rov.width()/4), int(self.rov.height()/4), self.rov)
    # #     self.ocean.translate(0, 10)#, Qt.TransformationMode.SmoothTransformation)
    # #     #     # self.rov.translate(10,0)
    # #     #     # sleep(1)
    #     print(1)

    #     painter.eraseRect(self.rov)

    #     self.rov.translate(20, 0)
    #     # # painter.update()
    #     painter.drawImage(self.rov, QImage('assets/rov2.png'))


    # def drawBezierCurve(self, qp):
    
    #     path = QPainterPath()
    #     path.moveTo(30, 30)
    #     path.cubicTo(30, 30, 200, 350, 350, 30)

    #     qp.drawPath(path)

## 




class SideBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

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
            print(words)

        self.controls = control.Control(self)

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.current_word)
        self.layout.addStretch()
        self.layout.addWidget(self.controls)

        # self.layout.setContentsMargins(0,0,0,0)
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
            print(self.controls.guesses.guesses)
            self.controls.guesses.update()



if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    window.show()

    print(window.size())

    app.exec()