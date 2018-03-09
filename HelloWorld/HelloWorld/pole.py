<<<<<<< HEAD
from disk import *
import turtle
=======
>>>>>>> master
class Pole(object):
    def __init__(self, name, x, y, thick=5, length=200, color="yellow"):
        self.name = name
        self.stack = []
        self.top = 0
        self.x = x
        self.y = y
        self.thick = thick
        self.length = length
        self.color = color

    def showpole(self):
        turtle.pu()
        turtle.goto(self.x, self.y)
        turtle.fillcolor(self.color)
        turtle.pd()
        turtle.seth(0)
        turtle.fd(self.thick/2)
        turtle.left(90)
        turtle.fd(self.length)
        turtle.left(90)
        turtle.fd(self.thick)
        turtle.left(90)
        turtle.fd(self.length)
        turtle.left(90)
        turtle.fd(self.thick/2)
        turtle.end_fill()
        turtle.pu()

    def pushdisk(self, disk):
        disk.newpos(self.x, self.y + disk.geth()*self.top)
        disk.showdisk()
        self.stack += [disk,]
        self.top += 1

    def popdisk(self):
        self.stack[-1].cleardisk()
        self.top -= 1
        s = self.stack[-1]
        self.stack.pop()
        return s
