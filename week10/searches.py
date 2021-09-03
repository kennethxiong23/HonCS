from math import *

def linearSearch(x, L):
    """ return True if x is in L, False if not """
    for item in L:
        if item == x:
            return True
    # only gets here if not found!
    return False

def binarySearch(x, L):
    low = 0
    high = len(L) - 1
    while True:
        mid = (high + low)//2
        listItem = L[mid]
        if x == listItem:
            return True
        elif x > listItem:
            low = mid + 1
        elif x < listItem:
            high = mid - 1
        if low > high:
            return False

if __name__ == "__main__":
    # put test code here
    L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = 5
    print("%3d  %s  %s" % (x, str(L), linearSearch(x, L)))
    x = 500
    print("%3d  %s  %s" % (x, str(L), linearSearch(x, L)))
    x = 5
    print("%3d  %s  %s" % (x, str(L), binarySearch(x, L)))
