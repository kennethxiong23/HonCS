"""
    Description: This program draws a design and then draws it recursively, 
                 progressively getting smaller and smaller
    Author: Kenneth
    Date: fall 2021
"""
from graphics import *
import sys

def drawRainbow(pt, size, win):
    """
    Purpose: Draws a rainbow
    Parameters: Central point(point obj), size(int), window(graphWin  obj)
    Return Val: none
    """
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "white"]
    for color in colors:
        ring = Circle(pt, size)
        ring.setFill(color)
        ring.setOutline(color)
        ring.draw(win)
        size -= (0.08 * size)

def recursiveRainbow(pt, level, size, win):
    """
    Purpose: Recursively draws a rainbow
    Parameters: central Point(point obj), degree of recursion(int), size of 
                rainbow(int), window(graphWin obj)
    Return Val: None
    """
    p1 = pt.clone()
    p1.move(-size,-size)
    p2 = pt.clone()
    p2.move(-size,size)	
    p3 = pt.clone()
    p3.move(size,size)
    p4 = pt.clone()
    p4.move(size,-size)

    drawRainbow(pt, size, win)
    if level > 1:
        recursiveRainbow(p1, level-1, size/2, win)
        recursiveRainbow(p2, level-1, size/2, win)
        recursiveRainbow(p3, level-1, size/2, win)
        recursiveRainbow(p4, level-1, size/2, win)

def main():
    win = GraphWin("h", 600, 600)
    win.setBackground("white")
    pt = Point(win.getWidth()/2,win.getHeight()/2)
    scale = int(sys.argv[1])
    if win.getWidth() < win.getHeight():
        recursiveRainbow(pt,scale, win.getWidth()/4, win)
    else:
        recursiveRainbow(pt,scale, win.getHeight()/4, win)
    click = win.getMouse()



main()