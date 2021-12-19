"""
    Description: Slider class
    Author: Kenneth
    Date: Fall 2021
"""
from graphics import *

def slider(circle, rectangle, win):

    center = circle.getCenter()
    click = win.getMouse()
    # clicker = win.checkMouse()
    clicky = win.test()
    # print(clicky.getX())
    if click.getX() <= p2.getX() and  click.getX() >= p1.getX():
            if click.getY() <= p2.getY() and  click.getY() >=p1.getY():
                print("hi")
                if win.test() != None:
                    clicky = clicky.getX()
                    dX = clicky - center.getX()
                    circle.move(dX, 0)
                
    return False

if __name__ == "__main__":
    print("hello")
    win = GraphWin("test", 500, 500)
    p1 = Point(100, 100)
    p2 = Point(200, 110)
    rectangle = Rectangle(p1, p2)
    rectangle.setFill("slate gray")
    rectangle.setOutline("slate gray")
    radius = (p2.getY() - p1.getY()) * 1.25
    circle = Circle(rectangle.getCenter(), radius)
    circle.setFill("black")
    rectangle.draw(win)
    circle.draw(win)
    firstcall = True
    while True:
        slider(circle, rectangle, win)
    win.getMouse()