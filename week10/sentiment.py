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
    """
    Purpose: Reads in the input files that contains all the reviews and seperates them into a
    list of individual words paired with their rating
    Paramters: Filename(str)
    Return Val: list of lists with individual words and their adjusted rating
    """
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
    """
    Purpose: Convert the rating from a 1-4 to -2-2
    Paramters: Orignal Rating(int)
    Return Val: Adjusted Score
    """
    score = rating - 2
    return score

def findWord(word,  knownWords):
    """
    Purpose: Check if word has already been stored in main list
    Paramters: word(str), words already stored in the main list(list)
    """
    for score in knownWords:
        if score[1] == word:
            return knownWords.index(score)
    return -1

def removeWords(stopWords, allReviews):
    """
    Purpose: remove all commons words from main list of words using binary search
    Paramters: name of stop words file(str), all reviews(list of lists)
    Return Val: None
    """
    readFile = open(stopWords)
    commonWords = []
    for word in readFile:
        word = word.strip()
        commonWords.append(word)

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
    """
    Purpose: Prints the 20 highest and lowers rated reviews
    Parameters: the main list of reviews(list of lists)
    return Val: none
    """
    print("top 20:")
    for review in reviews[:20]:
        print("%s: %s" %(review[0], review[1]))
    print("bottom 20:")
    for review in reviews[-20:]:
        print("%s: %s" %(review[0], review[1]))

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
    fileName = "movieReviews.txt"
    commonsWords = "stopwords.txt"

    allReviews = readReviews(fileName)
    removeWords(commonsWords, allReviews)

    sentimentScore = []
    for review in allReviews: #accumulator that creates the main list of words with score
        rating = review[0]
        for word in review[1]:
            index = findWord(word, sentimentScore)
            if index == -1: # if word is not aleady in list add it with its rating
                sentimentScore.append([rating, word])
            else: #otherwise, remove previous value and insert new
                score = sentimentScore[index][0] + rating
                sentimentScore[index][0] = score

    selectionSort(sentimentScore)
    printReviews(sentimentScore)

main()