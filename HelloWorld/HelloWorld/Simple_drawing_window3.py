import sys
from HelloWorld import Simple_drawing_window
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Simple_drawing_window3(Simple_drawing_window):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("rabbit.png")

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        
        p.setBrush(QColor(0,0,0))
        p.drawPie(50,100,100,100,0,180*32)
        p.setPen(QColor(200,120,0))
        p.setBrush(QColor(200,120,0))
        #p.drawPie(50,150,100,100,0,180*16)

        p.drawPolygon(
            QPoint(50,200), QPoint(150,200), QPoint(100,400),
            )

        p.drawPixmap(QRect(200,100,320,320), self.rabbit)
        p.end()

def main():
    app = QApplication(sys.argv)
    w= Simple_drawing_window3()
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
