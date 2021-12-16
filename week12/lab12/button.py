"""
    Description: Creates a button class
    Author: Kenneth
    Date: Fall 2021
"""
from graphics import *

class Button(object):
    """class for a single button object"""
    def __init__(self, shape, text, win):
        self.win = win
        self.shape = shape
        self.text = text
    
    def __string__(self):
        """fancy type for the shape object and text within"""
        print("%s with %s text" %(self.shape, self.text))

    def move(self, dx, dy):
        """moves the object around"""
        self.shape.move(dx, dy)
        return

    def setFill(color):
        """set fill of object color"""
        self.shape.setFill(color)
        return

    def setOuline(color):
        """set outline color of object"""
        self.shape.setOutline(color)
        return
    
    def getP1(self):
        """get p1 of object"""
        return self.shape.getP1()

    def getP2(self):
        """get p1 of object"""
        return self.shape.getP2()
    
    def getText(self):
        """returns the text in the button"""
        return self.text
    
    def setText(self, text):
        """set text inside of button"""
        self.text = text
        return

    def getCenter(self):
        """returns the center point of button"""
        return self.shape.getCenter()
    
    def getWidth(self):
        """get width of button"""
        return self.shape.getWidth()

    def draw(self, win):
        """draws button on window"""
        center = self.shape.getCenter()
        text = Text(center, self.text)
        # text.setWidth(self.getWidth())
        text.draw(win)
        self.shape.draw(win)
        return

    def onClick(self, callback):
        """check if button is pressed"""
        click = self.win.getMouse()
        print(click)
        topLeftPoint = self.shape.getP1()
        bottomRightPoint = self.getP2()
        print(click)
        print(topLeftPoint)
        print(bottomRightPoint)

        if click.getX() <= bottomRightPoint.getX() and  click.getX() >=topLeftPoint.getX():
            if click.getY() <= bottomRightPoint.getY() and  click.getY() >=topLeftPoint.getY():
                callback()
        else:
            return
def test2():
    print("hawdawdawdawdawdawdadawdawdi")
if __name__ == "__main__":
    win = GraphWin("test", 500, 500)
    p1 = Point(100,100)
    p2 = Point(200,200)
    rectancle = Rectangle(p1,p2)
    test =  Button(rectancle, "hawdawdawdawdawdawdadawdawdi", win)
    test.draw(win)
    test.onClick(test2)
    win.getMouse()