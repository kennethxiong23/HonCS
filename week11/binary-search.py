def binarySearch(x, ls):
    """
            Purpose: A recursive implementation of binary search.
            Parameters: x - the value to search for
                        ls - a list of values to search through (ls should be sorted)
            Return Val: True if x is in ls
    """
    if len(ls) == 0 :
        return False
    mid = len(ls)//2
    if ls[mid] == x:
        return True
    if x < ls[mid]:
       return binarySearch(x, ls[0:mid])
    else:
        return binarySearch(x, ls[mid + 1:])

def main():
    L=(1,2,3,4,5,6,7,8,9)
    print(binarySearch(12345,L))
main()