from random import shuffle

"""                       INSTRUCTIONS
        When you get this up and running, copy-paste your merge() and
        mergeSort() functions into your sorts.py file.
        This way, all of your sorting algorithms will be in one place.    """

def merge(leftL, rightL, L):
    """ Implement the merge() function below and you should be good to go """
    list = []
    i = 0
    while True:
        if len(leftL) == i:
            list.append(rightL[i:])
            return list
        elif len(rightL) == i:
            list.append(leftL[i:])
            return list
        if leftL[i] < rightL[i]:
            list.append(leftL[i])
            list.append(rightL[i])
        else:
            list.append(rightL[i])
            list.append(leftL[i])
        i+=1

def mergeSort(L):
    if len(L) > 1:
        half = len(L) // 2		 # split into two lists
        L1 = L[0:half]
        L2 = L[half:]
        mergeSort(L1)			 # sort each list
        mergeSort(L2)
        merge(L1,L2,L)		     # merge them back into one sorted list


def main():
    N = 10
    L = list(range(N))

    shuffle(L)
    print(L)
    mergeSort(L)
    print(L)
    assert L == list(range(N))
    print(L)

main()
