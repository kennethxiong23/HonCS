"""
    Desciprtion: calcualtes how long it takes for sorting alogorithm to run.
    name; Kenneth
    Date: fall 2021
"""
from sorts import *
from random import shuffle
from time import *
def main():
    N = int(input('N: '))
    L = []
    for i in range(N):
        L.append(i)
    shuffle(L)
    shuffledList = L.copy()


    bubbleT0 = time()
    bubbleSort(L)
    bubbleT1 = time()
    L = shuffledList.copy()

    insertT0 = time()
    insertionSort(L)
    insertT1 = time()
    L = shuffledList.copy()

    selectT0 = time()
    selectionSort(L)
    selectT1 = time()
    L = shuffledList.copy()
    
    pythonT0 = time()
    L.sort()
    pythonT1 = time()
    print(insertT1, insertT0)
    print("Bubble: %s\nInsertion: %s\n Selection: %s\n Python: %s" %(bubbleT1-bubbleT0, insertT1-insertT0, selectT1-selectT0, pythonT1-pythonT0))
main()