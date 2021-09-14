def sumList_iterative(L):
    """ Iterative function to accumulate all items in L and return the sum """
    sum = 0
    for num in L:
        sum += num
    return sum


def sumList_recursive(L):
    """ Recursive function to accumulate all items in L and return the sum """
    if len(L) == 0:
        return 0
    else:
        print(L)
        return L[-1] + sumList_recursive(L[0:-1])


def count_iterative(x, L):
    """ Iterative function to return how many of x are in L """
    count = 0
    for item in L:
        if item == x:
            count += 1
    return count


def count_recursive(x, L):
    """ Recursive function to return how many of x are in L """
    if len(L) == 0:
        return 0
    if x == L[-1]:
        return 1 + count_recursive(x, L[0:-1])
    return count_recursive(x, L[0:-1])
    


def main():
    L = [0,1,2]
    print("The sum of all items in list: %s = %d" % (L, sumList_iterative(L)))
    print("The sum of all items in list: %s = %d" % (L, sumList_recursive(L)))

    L = [1,2,8,2,2]
    x = 2
    print("%d appears in the list: %s %d times" % (x, L, count_iterative(x, L)))
    print("%d appears in the list: %s %d times" % (x, L, count_recursive(x, L)))


main()
