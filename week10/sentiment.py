"""
    Descriptions: This program takes a list of critic reviews from rotten tomatoes, and calculates
                            the sentiment behind the words. It will determine whether or not the 
                            words have a positive or negative connotation based on the reviews that
                            they are found in.
    Name: Kenneth
    Date: Fall 2021
"""

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

def removeWords(stopWords, allReviews):
    "remove common words - where r ur proper block commentssssssssss"
    readFile = open(stopWords)
    commonWords = []
    for word in readFile:
        word = word.strip()
        commonWords.append(word)
    for review in allReviews:
        keepWords = []
        for word in review[1]:
            if word not in commonWords:
                keepWords.append(word)
            review[1] = keepWords

def bubbleSort(listOfLists):
    """ This is the bubble sort algorithm:
            - given a list L
            - for every item in the list, compare to the item just to the right, swap if needed
            - keep doing the above until you go from one end of the list to the
              other and don't make any swaps!
    """
    for i in range(len(listOfLists)):
        for j in range(len(listOfLists) - 1):
            first = listOfLists[j][0]
            second  = listOfLists[j + 1][0]
            if first  > second:
                listOfLists[j][0], listOfLists[j + 1][0] = listOfLists[j + 1][0], listOfLists [j][0]
                listOfLists[j][1], listOfLists[j + 1][1] = listOfLists[j + 1][1], listOfLists [j][1]
    listOfLists.reverse()
    print(listOfLists)

def printReviews(reviews):
    print("top 20:")
    for review in reviews[:20]:
        print("%s: %s" %(review[0], review[1]))
    print("bottom 20:")
    for review in reviews[-20:]:
        print("%s: %s" %(review[0], review[1]))

def main():
    fileName = "movieReviews.txt"
    commonsWords = "stopwords.txt"
    allReviews = readReviews(fileName)
    removeWords(commonsWords, allReviews)
    sentimentScore = []
    for review in allReviews:
        rating = review[0]
        for word in review[1]:
            index = findWord(word, sentimentScore)
            if index == -1:
                sentimentScore.append([rating, word])
            else:
                score = sentimentScore.pop(index)
                sentimentScore.append([score[0] + rating, word])
    bubbleSort(sentimentScore)
    printReviews(sentimentScore)



        





main()