"""
    Description: This program visualizes how a sorting algorthim sorts through a list of numbers
    Name: Kenneth
    Date: Fall 2020
"""
from random import shuffle
from time import sleep

def generateList(length):
    """
    Purpose: Makes a random list with a specified length
    Parameters: Length of list(int)
    Return Val: A shuffled list of specified length
    """
    L = []
    for i in range(length):
        L.append(i)
    shuffle(L)
    return L

def printList(list, index, SWAP):
    """
    Purpose: Shows the two numbers that are being compared, if there is a swap, and the
    updated list.
    Parameters: The list(list), index that is being compared(int), and if there is a swap(bool)
    Return Val: None
    """
    stringList = []
    for i in range(len(list) ):
        if i == index or i == index + 1:
            stringList.append("|%s|" %list[i] )
        else:
            stringList.append(list[i])
    if SWAP:
        print("%s > %s SWAP!" %(list[index], list[index + 1]) )
        print("Current Pair:", *stringList)
        list[index], list[index + 1] = list[index + 1], list[index]
        print("updated list:", *list, end = "\n\n")

    else:
        print("%s <= %s NO SWAP!" %(list[index], list[index + 1]) )
        print("Current Pair:", *stringList)
        print("updated list:", *list, end = "\n\n")

def main():
    length = int(input("How long would you like the list to be: "))
    list = generateList(length)

    for i in range(len(list)):
        print("\n\n- - Pass #%s - -\n\n" %(i + 1))
        sleep(1.5) #Sleep so that user can see what swap it is on
        swaps = 0 #tracker to check when the sort is finished
        for j in range(len(list) - 1):
            first = list[j]
            second  = list[j + 1]
            if first  > second:
                swaps += 1
                printList(list, j, True)
            else:
                printList(list, j, False)
            sleep(0.75)#sleep to make each comparision linger so it can be seen
        if swaps == 0:
            break
        input("Hit enter to move onto the next pass")
    print("No more swaps, list is sorted: ", *list)
        


main()