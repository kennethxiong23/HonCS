from counter import *

class Clock(object):
    """ a 24-hour clock object, made of three counter objects: one for the seconds
        (0->59), one for the minutes (0->59), and one for the hour (0->23).  """

    def __init__(self, hour, min, sec):
        """ construct counter obj, given hours minutes and seconds """
        self.hour = Counter(24)
        self.hour.setValue(hour)
        self.min = Counter(60)
        self.min.setValue(min)
        self.sec = Counter(60)
        self.sec.setValue(sec)
        self.alarm = False

    ###  MORE METHODS TO BE IMPLEMENTED BY YOU  ###
    def __str__(self):
        return "Clock: %.2i:%.2i:%.2i" %(self.hour.value, self.min.value, self.sec.value)
    def setHour(self, hour):
        self.hour.setValue(hour)
    def setMinutes(self, min):
        self.min.setValue(min)
    def setSeconds(self, sec):
        self.sec.setValue(sec)

    def getHour(self):
        return self.hour.value

    def tick(self):
        self.sec.setValue(self.sec.value + 1)
        if self.sec.value == 0:
            self.min.setValue(self.min.value + 1)
            if self.min.value == 0:
                self.hour.setValue(self.hour.value +1)
    def getTime(self):
            return "%.2i:%.2i:%.2i" %(self.hour.value, self.min.value, self.sec.value)

    def setAlarm(self, hour, minute, second):
        if hour == self.hour.value:
            if minute == self.min.value:
                if second == self.sec.value:
                    self.alarm = True
    def inAlarm(self):
        return self.alarm






if __name__ == "__main__":
    c1 = Clock(12,55,21)
    print(c1)
    print("Setting time to 23:59:55...")
    c1.setHour(23)
    c1.setMinutes(59)
    c1.setSeconds(55)
    print("Hour for c1: %d" % (c1.getHour()))
    print(c1)
    for i in range(15):
        c1.tick()
        print(c1)
