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
        if leftL[i] <= rightL[j]:
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
    Return Val: list of every valid word
    """
    readFile = open(filename, 'r')
    words = []
    for line in readFile:
        line = line.strip()
        line = line.split()
        for word in line:
            word = word.lower()
            word = word.replace("'s","")
            word = word.replace("--", " ")
            if len(word) > 0:
                if word.isalpha():
                    words.append(word)
                else:
                    if word[:-1].isalpha():
                        words.append(word[:-1])
                    elif word[1:].isalpha():
                        words.append(word[1:])
    mergeSort(words)
    readFile.close()
    return(words)

def countWords( wordList):
    """
    Purpose: tallies up all the same words in a given list
    Paramters: list of all the word(list)
    Return Val: list of list with [string, value] pairs
    """
    
    wordAndValue = []
    sameWordStart = 0
    for index in range (len(wordList)):
        amount = index - sameWordStart + 1
        if index == len(wordList) - 1:
            amount = index - sameWordStart + 1
            wordAndValue.append([wordList[index], amount])
        else:
            if wordList[index] != wordList[index + 1]:
                wordAndValue.append([wordList[index], amount])
                sameWordStart = index + 1
    return wordAndValue

def writeList(filename, list):
    """
    Purpose: writes a list of word, value pairs to a file
    Parameters: Filename(str), list(list)
    Return Val: None
    """
    outFile = open(filename, "w")
    for item in list:
        outFile.write('%s,%s\n' %(item[0], item[1]))
    outFile.close()
    return

def addCount(inName, outName):
    """
    Purpose: Adds a list of word value pairs to a word counts file from another file
    Parameters: Filename(str), list(list)
    Return Val: None
    """
    infile = open(inName, "r")
    inList = []
    for line in infile:
        line = line.strip()
        line = line.split(",")
        inList.append(line)
    infile.close()
    outfile = open(outName, "r")
    outList = []
    for line in outfile:
        line = line.strip()
        line = line.split(",")
        outList.append(line)
    outfile.close()
    listIndex = 0
    writeString = ""
    for item in outList:
        if listIndex >= len(inList) - 1:
            break
        if item[0] < inList[listIndex][0]:
            writeString += ("%s,%s\n" %(item[0], item[1]))
        elif item[0] == inList[listIndex][0]:
             writeString += ("%s,%s\n" %(item[0], int(item[1]) + int(inList[listIndex][1])))
             listIndex += 1
        else:
            writeString += ("%s,%s\n" %(item[0], item[1]))
    outfile = open(outName, "w")
    outfile.write(writeString)
    outfile.close()
    return

def main():
    time1 = time()
    print(time())
    readList = readText("moby_dick.txt")
    valueList = countWords(readList)
    writeList("word-count-moby.txt", valueList)
    addCount("word-count-moby.txt", "wordCounts.txt")

    time2 = time()
    print(time2-time1)






main()