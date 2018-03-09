from HelloWorld import Simple_drawing_window
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Simple_drawing_window2(Simple_drawing_window):
    def __init__(self):
        return super().__init__()

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))

        p.drawPolygon(
            QPoint(70,100),QPoint(100,110),
            QPoint(130,100), QPoint(100,150), 
            )
        p.setPen(QColor(255,127,0))
        p.setBrush(QColor(255,127,0))
        p.drawPie(30,150,150,150,0,180*32)


        p.drawPixmap(QRect(200,100,320,320), self.rabbit)
        p.end()

def main():
    app = QApplication(sys.argv)
    w= Simple_drawing_window2()
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
