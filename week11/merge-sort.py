
"""                       INSTRUCTIONS
        When you get this up and running, copy-paste your merge() and
        mergeSort() functions into your sorts.py file.
        This way, all of your sorting algorithms will be in one place.    """
from random import shuffle

def merge(leftL, rightL, L):
    """ Implement the merge() function below and you should be good to go """
    i = 0
    j = 0
    index = 0
    while i < len(leftL) and j < len(rightL):
        if leftL[i][0] <= rightL[j][0]:
            L[index] = leftL[i]
            i += 1
        else:
            L[index] = rightL[j]
            j += 1
        index += 1
    while i < len(leftL):
        L[index] = leftL[i]
        i += 1
        index += 1
    while j < len(rightL):
        L[index] = rightL[j]
        j += 1
        index += 1  

def mergeSort(L):
    if len(L) > 1:
        half = int(len(L) / 2)		 # split into two lists
        L1 = L[0:half]
        L2 = L[half:]
        mergeSort(L1)			 # sort each list
        mergeSort(L2)
        merge(L1,L2,L)		     # merge them back into one sorted list


def main():

    N = 10
    L = [[1,2],[2,2],[3,2],[4,5],[5,65]]

    shuffle(L)
    print(L)
    mergeSort(L)
    print(L)

main()