"""coin flip using recursion, countes the amount of times that heads occured"""

import random
import sys
sys.setrecursionlimit(2147483647)
def countHeads(flips):
    if flips <= 0 :
        return 0
    else:
        FLIP = random.randrange(0,2)
        totalHeads = FLIP + countHeads(flips -1)
    return totalHeads

def main():
    flips = int(input("how many times would you like the flip the coin? "))
    print("that happend %s times" %countHeads(flips))

main()