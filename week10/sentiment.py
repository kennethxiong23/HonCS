"""
    Descriptions: This program takes a list of critic reviews from rotten tomatoes, and calculates
                            the sentiment behind the words. It will determine whether or not the 
                            words have a positive or negative connotation based on the reviews that
                            they are found in.
    Name: Kenneth
    Date: Fall 2021
"""
# def readLine(filename):
#     """open given filename, read in text, split into words, return list of words"""
#     readFile = open(filename)
#     words = []
#     for line in readFile:
#         line = line.strip()
#         words.append(line)

#     return words
from os import remove

def readFile(fileName):
    readFile = open(fileName)
    ratingAndWords = []
    for line in readFile:
        line = line.strip()
        line = line.split()
        rating = convertScore(int(line[0]))
        words = line[1:]
        ratingAndWords.append([rating, words])
    return ratingAndWords

def convertScore(rating):
    """convert the score from 1-5 to -2-2"""
    score = rating - 3
    return score

def findWord(word,  knownWords):
    """check if word has already been stored"""
    for score in knownWords:
        if score[1] == word:
            return knownWords.index(score)
    return -1

def removeWords(commonWords, allWords):
    "remove common words - where r ur proper block commentssssssssss"
    commonWords = open("stopwords")
    commonWords = commonWords.strip()
    print(commonWords)

def main():
    removeWords(se)
    fileName = "smallReviews.txt"
    allReviews = readFile(fileName)
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
    print(sentimentScore)


        





main()