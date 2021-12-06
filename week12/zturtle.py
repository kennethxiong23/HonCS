"""
    Description: turtle class using Zelle graphics (only partially complete).
    Author: Mr. Bloom
    Date: Spring 2020
"""

from graphics import *
from math import *
from time import sleep

###############################################################

class ZTurtle(object):
    """ Zelle Graphics Turtle """
    def __init__(self, x, y, win):
        self.x = x
        self.y = y
        self.heading = 0
        self.tailup = False
        self.window = win
        self.color = 'white'
    def __str__ (self):
        return "x=" + str(self.x) + ", y=" + str(self.y) + "heading=" + str(self.heading) + "tailup=" + str(self.tailup)

    def down(self):
        self.tailup = False

    def setColor(self, color):
        self.color = color

    def setHeading(self, heading):
        self.heading = heading

    def turn(self, angle):
        self.heading += angle

    def up(self):
        self.tailup = True

    def window(self, window):
        self.win = window

    def moveTo(self, x, y):
        self.x = x
        self.y = y

    def dot(self):
        dot = Point(self.x, self.y)
        dot.draw(self.window)

    # you need to write:
    #
    # __init__    construct new turtle, given x,y coords and graphics win
    #             hint...use these instance variables:
    #
    #             self.x          current x position
    #             self.y          current y position
    #             self.heading    current heading (0 means East,90 North)
    #             self.tailup     True if tail is up, False if down
    #             self.window     the graphics window for drawing
    #             self.color      color used for drawing
    #
    # __str__     return string with x,y,heading, and tail up or down
    # setColor    change color of pen
    # setHeading  set turtle direction
    # turn        alter turtle direction by certain angle
    # down        put tail down
    # up          lift tail up
    # moveto      magically move turtle to location x,y (no drawing)
    # dot         drop a visible marker at current location


    def forward(self, ds):
        """ move forward a distance ds, draw if tail is down """
        curr_pt = Point(self.x, self.y)
        theta = radians(self.heading)
        dx = ds * cos(theta)
        dy = ds * sin(theta)
        nx = self.x + dx
        ny = self.y + dy
        new_pt = Point(nx, ny)
        if not self.tailup:
            L = Line(curr_pt, new_pt)
            L.draw(self.window)
            L.setFill(self.color)
            sleep(0.1)
        self.x = nx
        self.y = ny


#------------------------------------------------------------------------------#

if __name__ == "__main__":
    gw = GraphWin("zturtle test", 500, 500)
    gw.setBackground("gray")
    t = ZTurtle(100,100,gw)
    print(t)
    t.setColor("red")
    t.down()
    t.forward(100)
    gw.getMouse()
