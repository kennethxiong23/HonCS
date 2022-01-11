from random import shuffle
def binarySearch(word, list):
    """
    Purpose: Binary search
    Parameters: Word be searched for in list(str), list of words being searched in (list)
    return Val: Boolean depending on if word is in the list
    """
    low = 0
    high = len(list) - 1
    while True:
        mid = (high + low)//2
        listItem = list[mid][0]
        if word == listItem:
            return mid
        elif word > listItem:
            low = mid + 1
        elif word < listItem:
            high = mid - 1
        if low > high:
            return False
        
def main():
    L = [['a', 1], ['b', 2],['c', 4]]
    print(type(L))
    print(L)
    print(binarySearch('a', L))
main()