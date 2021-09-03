"""
    Description:
    Author:
    Date:
"""

#------------------------------------------------------------------------------#
def mySort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            first = L[j]
            second  = L[j + 1]
            if first  > second:
                L[j], L[j + 1] = L[j + 1], L [j]
    return L


#------------------------------------------------------------------------------#
def bubbleSort(L):
    """ This is the bubble sort algorithm:
            - given a list L
            - for every item in the list, compare to the item just to the right, swap if needed
            - keep doing the above until you go from one end of the list to the
              other and don't make any swaps!
    """
    for i in range(len(L)):
        for j in range(len(L) - 1):
            first = L[j]
            second  = L[j + 1]
            if first  > second:
                L[j], L[j + 1] = L[j + 1], L [j]
    return L


#------------------------------------------------------------------------------#
def selectionSort(L):
    """ This is the selection sort algorithm:
            - given a list L
            - find the smallest number in the list, swap it to position 0
            - find the next smallest number in the list, swap it to position 1
            - find the next smallest number in the list, swap it to position 2
            - And so on...

        NOTE: It is called selection sort because, each time, you are selecting
        the smallest number from the remaining unsorted elements.
    """
    spot = 0
    for i in range(len(L)):
        index = spot
        for j in range(spot, len(L)):
            if L[j] < L[index]:
                index = j
        L[index], L[spot] = L[spot], L[index]
        spot += 1
    return L







#------------------------------------------------------------------------------#
def insertionSort(L):
#     """ This is the insertion sort algorithm:
#             - assume item at index 0 is already "sorted"
#             - starting with item at index 1, check all items to the left and swap positions if needed
#             - do the same for item at index 2, where now items at index 0 and 1 should be in order
#             - do the same for item at index 3, where now items at index 0, 1, and 2 are in order...and so on

#         NOTE: Notice that, for each index, all items to the left are in order, and you are inserting the next item into the correct spot.
#     """
    for i in range (1, len(L)):
        index = i -1 
        marker = L[i]
        while index >= 0 and marker < L[index]:
            L[index + 1] = L[index]
            index -= 1
        L[index+1] =  marker
    return L
    



#------------------------------------------------------------------------------#
if __name__ == "__main__":

    from random import shuffle

    N = 10
    L = []
    listCopy = []
    for i in range(N):
        L.append(i)
        listCopy.append(i)

    shuffle(L)
    insertionSort(L)
    assert L == listCopy
