"""
    Description: This program visualizes how a sorting algorthim sorts through a list of numbers
    Name: Kenneth
    Date: Fall 2020
"""
from random import shuffle

def main():
    L = [1,2,3,4,5,6,7]
    L = shuffle(L)
    print(L)
    for i in range(len(L)):
        for j in range(len(L) - 1):
            first = L[j]
            second  = L[j + 1]
            if first  > second:
                L[j], L[j + 1] = L[j + 1], L [j]

    print(L)



main()