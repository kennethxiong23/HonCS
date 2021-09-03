"""
    Descriptions: This program takes a list of critic reviews from rotten tomatoes, and calculates
                            the sentiment behind the words. It will determine whether or not the 
                            words have a positive or negative connotation based on the reviews that
                            they are found in.
    Name: Kenneth
    Date: Fall 2021
"""
from time import time
def readReviews (fileName):
    readFile = open(fileName)
    ratingAndWords = []
    for line in readFile:
        line = line.lower()
        line = line.strip()
        line = line.split()
        rating = convertScore(int(line[0]))
        words = line[1:]
        ratingAndWords.append([rating, words])
    return ratingAndWords

def convertScore(rating):
    """convert the score from 1-5 to -2-2"""
    score = rating - 2
    return score

def findWord(word,  knownWords):
    """check if word has already been stored"""
    for score in knownWords:
        if score[1] == word:
            return knownWords.index(score)
    return -1

def removeWords(stopWords, word):
    "remove common words - where r ur proper block commentssssssssss"
    readFile = open(stopWords)
    commonWords = []
    for stopWord in readFile:
        stopWord = stopWord.strip()
        commonWords.append(stopWord)
    if word.isalpha() == True:
        if binarySearch(word, commonWords) == False:
            return True
    return False

    for review in allReviews:
        keepWords = []
        for word in review[1]:
            if word.isalpha() == True:
                if binarySearch(word, commonWords) == False:
                    keepWords.append(word)
            review[1] = keepWords

def selectionSort(listOfLists):
    """ This is the selection sort algorithm:
            - given a list L
            - find the smallest number in the list, swap it to position 0
            - find the next smallest number in the list, swap it to position 1
            - find the next smallest number in the list, swap it to position 2
            - And so on...

        NOTE: It is called selection sort because, each time, you are selecting
        the smallest number from the remaining unsorted elements.
    """
    spot = 0
    for i in range(len(listOfLists)):
        index = spot
        for j in range(spot, len(listOfLists)):
            if listOfLists[j][0] < listOfLists[index][0]:
                index = j
        listOfLists[index][0], listOfLists[spot][0] = listOfLists[spot][0], listOfLists [index][0]
        listOfLists[index][1], listOfLists[spot][1] = listOfLists[spot][1], listOfLists [index][1]
        spot += 1
    listOfLists.reverse()
    return listOfLists

def printReviews(reviews):
    print("top 20:")
    for review in reviews[:20]:
        print("%s: %s" %(review[0], review[1]))
    print("bottom 20:")
    for review in reviews[-20:]:
        print("%s: %s" %(review[0], review[1]))

def binarySearch(word, list):
    low = 0
    high = len(list) - 1
    while True:
        mid = (high + low)//2
        listItem = list[mid]
        if word == listItem:
            return True
        elif word > listItem:
            low = mid + 1
        elif word < listItem:
            high = mid - 1
        if low > high:
            return False

def main():
    t0 =time()
    fileName = "1000Reviews.txt"
    commonsWords = "stopwords.txt"
    allReviews = readReviews(fileName)
   # removeWords(commonsWords, allReviews)
    sentimentScore = []
    for review in allReviews:
        rating = review[0]
        for word in review[1]:
            if removeWords(commonsWords, word):
                index = findWord(word, sentimentScore)
                if index == -1:
                    sentimentScore.append([rating, word])
                else:
                    score = sentimentScore.pop(index)
                    sentimentScore.append([score[0] + rating, word])
    t1 = time()
    selectionSort(sentimentScore)
    t2 = time()
    printReviews(sentimentScore)
    print("runtime: \nlist formating: %s\nSorting: %s" %(t1-t0, t2-t1))

main()