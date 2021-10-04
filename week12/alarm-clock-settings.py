from graphics import *
from clock import *
from time import sleep
from os.path import isfile


def main():
    if isfile("user-alarm.txt"):
        alarm = open("user-alarm.txt", "r")
        line = alarm.read(3)
        line = line.strip()
        hour = int(line[0])
        minute = int(line[1])
        second = int(line[2])
    else:
        print("set an alarm")
        hour = int(input("Hour:"))
        minute = int(input("Minutes:"))
        second = int(input("Seconds:"))
        alarm = open("user-alarm.txt", "w")
        alarm.write("%0.2i%0.2i%0.2i" %(hour, minute, second))

    width = 300
    height = 100
    gw = GraphWin("digital clock", width, height)
    gw.setBackground("black")

    hours = 0
    minutes = 0
    seconds = 0
    digClock = Clock(hours, minutes, seconds)

    while True:
        # get current time and display clock
        time = digClock.getTime()
        clockText = Text(Point(width/2, height/2), time)
        clockText.setSize(36)
        clockText.setOutline("green")
        clockText.draw(gw)
        digClock.setAlarm(hour, minute, second)
        if digClock.inAlarm():
	        gw.setBackground('red')


        sleep(0.9)        # sleep for 1 second and tick the clock forward one sec
        digClock.tick()

        clockText.undraw()  # undraw old time, so can display the new time

        if gw.checkMouse():
            break

    gw.close()

main()
