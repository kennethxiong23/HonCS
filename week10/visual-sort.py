"""
    Description: This program visualizes how a sorting algorthim sorts through a list of numbers
    Name: Kenneth
    Date: Fall 2020
"""
from random import shuffle

def generateList(length):
    """make a random list with specified length"""
    L = []
    for i in range(length):
        L.append(i)
    shuffle(L)
    return L

def printList(list, index, SWAP):
    """Shows the visual aspect of if it's switched or not"""
    stringList = []
    for i in range(len(list) ):
        if i == index or i == index + 1:
            stringList.append("|%s|" %list[i] )
        else:
            stringList.append(list[i])
    if SWAP:
        print
    print(*stringList)


def main():
    length = int(input("How long would you like the list to be: "))
    list = generateList(length)

    for i in range(len(list)):
        print("Pass #%s" %(i + 1))
        for j in range(len(list) - 1):
            first = list[j]
            second  = list[j + 1]
            if first  > second:
                printList(list, j, True)
                list[j], list[j + 1] = list[j + 1], list[j]
            else:
                printList(list, j, False)

        
    print(list)




main()