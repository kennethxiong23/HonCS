"""
    Description: Normal swindle program but save prefences of the user
    Author: Kenneth
    Date: Fall 2021
"""
from book import *

def readBookDatabase(filename):
    """ read in book info from bookdb.txt, save each line as a Book object in list.
        This list will be returned and will serve as availableBooks. """
    infile = open(filename, 'r')
    availableBooks = []
    for book in infile:
        book = book.strip()
        info = book.split(",")
        book = Book(info[0], info[1], info[2], info[3])
        availableBooks.append(book)
    infile.close()
    return availableBooks


def checkList(list, str):
    """Gets the user input for a number, and checks to see if there is a book at that position"""
    while True:
        userInput = input(str)
        try:
            num = int(userInput)
            if 0 <= num <= len(list):
                return num
            else:
                print("invalid number, try again")
        except ValueError:
            print("invalid input, try again")
            

class Swindle(object):
    """ class for a single Swindle object """

    def __init__(self, owner):
        """ constructor for swindle object, given owner """
        self.availableBooks = readBookDatabase("bookdb.txt")
        self.owner = owner
        self.ownedBooks = []
        self.pageLength = 20

    def __str__(self):
        """ pretty-print info about this object """
        ###  TO BE COMPLETED BY YOU  ###
        s = "available books: %s, owner: %s, owned books: %s, page len: %s" %(self.availableBooks,
        self.owner, self.ownedBooks, self.pageLength)
        return s

    def getLetter(self):
        """ This method determines what the user wants to do next """
        validChoices = ['n', 'p', 'q']
        while True:
            readingChoice = str(input("\nn (next); p (previous); q (quit): "))
            if readingChoice in validChoices:
                return readingChoice
            print("invalid input, try again")

    def displayPage(self, book):
        """ This method displays a single page at a time (300 chars) """
        bookContents = book.getText()
        bookLinesList = bookContents.split("\n")
        numLines = len(bookLinesList)
        numPages = numLines // self.pageLength  # calculate total number of pages in book
        page = book.getBookmark()               # get current page (most recently read)
        pageStart = page * self.pageLength
        pageEnd = pageStart + self.pageLength   # display 20 lines per page
        if pageEnd > numLines:
            pageEnd = numLines                  # in case you're at the end of the book
        for i in range(pageStart, pageEnd):
            print(bookLinesList[i])
        if numPages == 1:                       # alter page numbers for 1-page books
            page = 1
        print("\nShowing page %d out of %d" % (page, numPages))
        return

    def displayText(self, book):
        """ This method allows the user to read one of their books.
            It calls displayPage() to show a single page at a time.
            It calls getLetter() to determine what the user wants to do next.
            When the user decides to quit reading a particular book, this method
            returns the (updated) Book object.
        """
        while True:
            self.displayPage(book)
            currentPage = book.getBookmark()
            choice = self.getLetter()       # user chooses to quit or read the next/previous page
            if choice == "q":               # quit reading and return to ereader
                return book
            elif choice == "n":                 # move on to the next page in the book
                bookContents = book.getText()   # unless user is on the last page
                numLines = bookContents.count("\n")
                currentLine = currentPage * self.pageLength
                if (currentLine + 1) < (numLines - self.pageLength):
                    book.setBookmark(currentPage+1)
                else:
                    print("\nThere are no more pages. Enter 'p' to go to the previous page or 'q' to quit.")
            else:                               # return to previous page in the book
                book.setBookmark(currentPage-1)
        return

    def showOwned(self):
        """prints all the books that the owner owns"""
        if len(self.ownedBooks) == 0:
            print("You don't own any books!")
        else:
            for index in range(len(self.ownedBooks)):
                print("%d:%s" %(index + 1, self.ownedBooks[index].toString()))
    
    def showAvailable(self):
        """show available books to be bought"""
        if len(self.availableBooks) == 0:
            print("No books are available to be bought.")
        else:
            for index in range(len(self.availableBooks)):
                print("%d:%s" %(index + 1, self.availableBooks[index].toString()))
    
    def getOnwer(self):
        return self.owner

    def buy(self):
        """allows user to buy book from available books"""
        self.showAvailable()
        prompt ="\nWhich book would you like to buy? (0 to skip): "
        bookNum = checkList(self.availableBooks, prompt)
        if bookNum >= 1:
            ownedBook = self.availableBooks.pop(bookNum-1)
            self.ownedBooks.append(ownedBook)
            print("\nYou've successfully purchased the book: %s" %ownedBook.getTitle())
    
    def read(self):
        """allows the user to read a book"""
        self.showOwned()
        if len(self.ownedBooks) > 0:
            prompt = "\nWhich book would you like to read? (0 to skip): "
            bookNum = checkList(self.ownedBooks, prompt)
            if bookNum >= 1:
                userBook = self.ownedBooks[bookNum-1]
                self.displayText(userBook)
                print("\nSetting bookmark in %s at page %i" 
                    %(userBook.getTitle(), userBook.getBookmark()))

if __name__ == '__main__':
    print("Testing the Swindle class...")
    owner = "Lionel"
    myswindle = Swindle(owner)
    print(myswindle)

    print("Testing showAvailable...")
    myswindle.showAvailable()

    print("Testing showOwned...")
    myswindle.showOwned()

    print("testing getOnwer")
    print(myswindle.getOnwer)
    
    print("testing buy")
    myswindle.buy()
    
    print("testing read")
    myswindle.read()

