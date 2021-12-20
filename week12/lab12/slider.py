"""
    Description: Slider class
    Author: Kenneth
    Date: Fall 2021
"""
from graphics import *
class Slider(object):
    """class for a single slider object"""
    def __init__(self, rectangle, rectColor, circColor, win):
        self.center = rectangle.getCenter()
        self.rectangle = rectangle
        self.rectangle.setFill(rectColor)
        self.rectangle.setOutline(rectColor)
        self.radius = (p2.getY() - p1.getY()) * 1.25
        self.circle = Circle(self.center,  self.radius )
        self.circle.setFill(circColor)
        self.circle.setOutline(circColor)
        self.holdingSlider = False
        self.win = win
    
    def __string__(self):
        """fancy type for the shape object and text within"""
        print("rectange top left is at %s, circle is at %s." %(self.rectangle.p1(), self.circle.getCenter()))          

    def move(self, dx, dy):
        """moves the slider around"""
        self.rectangle.move(dx, dy)
        self.circle.move(dx, dy)
        return

    def setRectFill(self, color):
        """set fill of rectangle color"""
        self.rectangle.setFill(color)
        return

    def setRectOuline(self, color):
        """set outline color of rectange"""
        self.rectangle.setOutline(color)
        return
    
    def getRectP1(self):
        """get p1 of rectangle"""
        return self.rectangle.getP1()

    def getRectP2(self):
        """get p1 of rectangle"""
        return self.rectangle.getP2()

    def getRectCenter(self):
        """returns the center point of button"""
        return self.rectangle.getCenter()

    def setCircFill(self, color):
        """set fill of circle color"""
        self.circle.setFill(color)
        return

    def setCircOuline(self, color):
        """set outline color of circle"""
        self.circle.setOutline(color)
        return
    
    def getCircP1(self):
        """get p1 of circle"""
        return self.circle.getP1()

    def getCircP2(self):
        """get p1 of circle"""
        return self.circle.getP2()

    def getCircCenter(self):
        """returns the center point of button"""
        return self.circle.getCenter()

    def onClick(self):
        """returns the positon of the slider"""
        click = self.win.checkMouse()
        if click != None:   #check if clicking the circle or not
            #check initially is mouse is on circle
            if click.getX() <= p2.getX() and  click.getX() >= p1.getX():
                    if click.getY() <= p2.getY() and  click.getY() >= p1.getY():
                        self.holdingSlider = True
                        dX = click.getX() - self.circle.getCenter().getX()
                        self.circle.move(dX, 0)
            #if mouse moves off circle, but still holding down, still move slider
            if click.getX() <= p2.getX() and  click.getX() >= p1.getX():
                if self.holdingSlider == True and self. win.getMouseUp() == True:
                    dX = click.getX() - self.circle.getCenter().getX()
                    self.circle.move(dX, 0)
        #once it is released, make sure it is no longer holding slider
        if self.win.getMouseUp() == False:
            self.holdingSlider = False
    
    def getValue(self):
        """returns the value 0-1 that coresponds to the position on the slider"""
        min = self.getRectP1().getX()
        max = self.getRectP2().getX()
        val = min - self.circle.getCenter().getX()
        adjustedVal = val/(min-max)
        return adjustedVal
                    
    def draw(self):
        """draws button on window"""
        self.rectangle.draw(self.win)
        self.circle.draw(self.win)
        return

if __name__ == "__main__":
    print("hello")
    win = GraphWin("test", 500, 500)
    p1 = Point(100, 100)
    p2 = Point(200, 110)
    rectangle = Rectangle(p1, p2)
    slider = Slider(rectangle, "slate gray", "black", win)
    slider.draw()
    while True:
        slider.onClick()
        print(slider.getValue())


