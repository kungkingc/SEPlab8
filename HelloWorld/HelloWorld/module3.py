from turtle import *

class Disk:
    def __init__(self, name, xpos, ypos, height = 20, width = 100, color = "Black"):
        self.name = name
        self.xpos = xpos
        self.ypos = ypos

    def showdisk(self):
        pendown()
        forward(width/2)
        left(90)
        forward(height)
        left(90)
        forward(width)
        left(90)
        forward(height)
        left(90)
        forward(width/2)

    def newpos(self, x, y):
        self.xpos = x
        self.ypos = y

    def cleardisk(self):


showdisk()