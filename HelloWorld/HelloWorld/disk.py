from turtle import *

<<<<<<< HEAD


class Disk(object):

    def __init__(self, dname, xpos, ypos, dh, dw, col = "red"):

        self.name = dname

        self.x = xpos

        self.y = ypos

=======
class Disk(object):
    def __init__(self, dname, xpos, ypos, dh, dw, col = "red"):
        self.name = dname
        self.x = xpos
        self.y = ypos
>>>>>>> ba3f0c2bc38191b10be9e8b6d8ad0649849f5c8a
        self.h = dh

        self.w = dw

        self.color = col



    def showdisk(self):

        pu()

        goto(self.x, self.y)

        pd()

        fillcolor(self.color)

        begin_fill()

        seth(0)

        fd(self.w / 2)

        lt(90)

        fd(self.h)

        lt(90)

        fd(self.w)

        lt(90)

        fd(self.h)

        lt(90)

        fd(self.w / 2)

        end_fill()



    def newpos(self,x,y):

        self.x = x

        self.y = y



    def cleardisk(self):

        pu()

        goto(self.x,self.y)

        pd()

        fillcolor("white")

        pencolor("white")

        begin_fill()

        seth(0)

        fd(self.w / 2)

        lt(90)

        fd(self.h)

        lt(90)

        fd(self.w)

        lt(90)

        fd(self.h)

        lt(90)

        fd(self.w / 2)

        end_fill()

        pencolor("black")

        fillcolor(self.color)



    def getx(self):

        return self.x



    def gety(self):

        return self.y



    def getname(self):

        return self.name



    def geth(self):

        return self.h



    def getw(self):

        return self.w