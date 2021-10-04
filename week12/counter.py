class Counter(object):
    """ An object that keeps track of some value, where the value starts at zero,
        counts up to some maximum value, and then resets back to zero. """
    def __init__(self, max):
        self.max = max
        self.value = 0

    def __str__(self):
        return "Value: " + str(self.value) + "  (MaxValue = " + str(self.max) +")"
    def increment(self):
        self.value += 1
        if self.value >= self.max:
            self.value = 0
    def setValue(self, value):
        self.value = value
        if self.value >= self.max:
            self.value = 0






if __name__ == "__main__":      # test code goes here for custom Classes

    c = Counter(60)
    print(c)
    for i in range(10):
        c.increment()
        print(c)

    print("-" * 20)
    print("set counter value to 55")

    c.setValue(55)
    print(c)
    for i in range(10):
        c.increment()
        print(c)
