def maxList(L):
    if len(L) == 0:
        return 0
    else:
        if L[-1] > maxList(L[:-1]):
            return L[-1]
        else:
            return maxList(L[:-1])
def main():
    L = [9,4,5,2,5,1,54,7,1,4,6,7,5,3,52,3234]
    print(maxList(L))

main()