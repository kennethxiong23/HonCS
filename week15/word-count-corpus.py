"""
    Description: This program finds all occurences of a word in a book and then adds them 
    to a list of all word counts in alphabetical order.
    Author: Kenneth
    Date: Spring 2022
"""
from string import punctuation
from time import time

def merge(leftL, rightL, L):
    """
    Purpose: Merge two lists
    Parameters: leftL(list), rightL(list), L(list)
    Return Val: None
    """
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
    """
    Purpose: Merge sort algorithm
    Parameters: L(list)
    Return Val: None
    """
    if len(L) > 1:
        half = int(len(L) / 2)		 # split into two lists
        L1 = L[0:half]
        L2 = L[half:]
        mergeSort(L1)			 # sort each list
        mergeSort(L2)
        merge(L1,L2,L)		     # merge them back into one sorted list


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

def readText(filename):
    """
    Purpose: Reads in the input file that contains the full text of a book
    Paramters: Filename(str)
    Return Val: list of lists with individual words and how many times they occured
    """
    readFile = open(filename, 'r')
    time0 = time()
    words = []
    num = 0
    for line in readFile:
        line = line.strip()
        line = line.split()
        for word in line:
            num += 1
            if num == 100000:
                print(num, time()-time0)
            if num == 10000:
                print(num, time()-time0)
            if num == 20000:
                print(num, time()-time0)
            if num == 50000:
                print(num, time()-time0)
            if len(words) == 0:
                if word.isalpha():
                    words.append([word, 1])
                else:
                    if word[0].isalpha() == False or word[-1].isalpha() == False:
                        if word[0].isalpha == False:
                            word = word[1:]
                        else:
                            word == word[:-2]
            else:
                index =  findWord(word, words)
                if index == -1: #add new word to list
                    if word.isalpha():
                        words.append([word, 1])
                    else:
                        if word[0].isalpha() == False or word[-1].isalpha() == False:
                            if word[0].isalpha == False:
                                word = word[1:]
                            else:
                                word == word[:-2]
                    # mergeSort(words)
                else:
                    words[index][1] += 1
    return words

def findWord(word,  knownWords):
    """
    Purpose: Check if word has already been stored in main list
    Paramters: word(str), words already stored in the main list(list)
    """
    for index in range(0, len(knownWords)):
        if word == knownWords[index][0]:
            if word == "whalemen":
                print("hi")
            return index
        else:
            if len(word) > 0:
                if word[0].isalpha() == False or word[-1].isalpha() == False:
                    if word[0].isalpha() == False:
                        word = word[1:]
                    elif word[-1].isalpha() == False:
                        word = word[:-1]
                    else:
                        word = word[1:-1]
                if word == knownWords[index][0]:
                    return index
                else:
                    if word.lower() == knownWords[index][0] :
                        return index
    return -1

def main():
    time1 = time()
    print(time())
    readList = readText("moby_dick.txt")
    print(mergeSort(readList))
    print(readList)

    time2 = time()
    print(time2-time1)






main()