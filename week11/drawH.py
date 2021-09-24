"""
draw H
"""
from graphics import *
import sys
def drawH(pt, level, size, win):
    p1 = pt.clone()
    p1.move(-size,-size)
    p2 = pt.clone()
    p2.move(-size,size)
    leftedge = Line(p1,p2)   		
    p3 = pt.clone()
    p3.move(size,size)
    p4 = pt.clone()
    p4.move(size,-size)
    rightedge = Line(p3,p4)
    p5 = pt.clone()
    p5.move(size, 0)
    p6 = pt.clone()
    p6.move(-size, 0)
    middlelines = Line(p5,p6)
    leftedge.draw(win)
    rightedge.draw(win)
    middlelines.draw(win)
    if level > 1:
        drawH(p1, level-1, size/2, win)
        drawH(p2, level-1, size/2, win)
        drawH(p3, level-1, size/2, win)
        drawH(p4, level-1, size/2, win)


def main():
    win = GraphWin("h", 600, 600)
    pt = Point(win.getWidth()/2,win.getHeight()/2)
    scale = int(sys.argv[1])
    if win.getWidth() < win.getHeight():
        drawH(pt,scale, win.getWidth()/4, win)
    else:
        drawH(pt,scale, win.getHeight()/4, win)
    click = win.getMouse()



main()