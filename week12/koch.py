from zturtle import *
from graphics import *

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            print(t)
            koch(t, order-1, size/3)
            t.turn(angle)
    

def main():
    gw = GraphWin("zturtle test", 800, 600)
    gw.setBackground("black")

    turtle = ZTurtle(100, 100, gw)
    koch(turtle,5, 500)
    gw.getMouse()


main()
