from book import *
from os.path import isfile
from graphics import *
from button import *
from swindle import *

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

    def __init__(self, owner, ownedBooks, avaliableBooks, win):
        """ constructor for swindle object, given owner """
        if avaliableBooks == []:
            self.availableBooks = readBookDatabase("bookdb.txt")
        else:
            self.availableBooks = avaliableBooks
        self.owner = owner
        self.ownedBooks = ownedBooks
        self.pageLength = 20
        self.win = win
        self.width = win.getWidth()
        self.height = win.getHeight()
        if self.width == 375:
            self.textSize = 8
        elif self.width == 450:
            self.textSize = 9
        else:
            self.textSize == 12

    def __str__(self):
        """ pretty-print info about this object """
        ###  TO BE COMPLETED BY YOU  ###
        s = "available books: %s, owner: %s, owned books: %s, page len: %s" %(self.availableBooks,
        self.owner, self.ownedBooks, self.pageLength)
        return s

    def changePage(self, page, numPage, book):
        #create forward and back buttons
        forCirc = Circle(Point(self.width * 0.8, self.height* 0.9), self.width * 0.05)
        backCirc = Circle(Point(self.width * 0.2, self.height* 0.9), self.width * 0.05)
        forwardButton = Button(forCirc, "→", self.win)
        backBut = Button(backCirc, "←", self.win)
        forwardButton.draw()
        backBut.draw()
        #edge cases for when you shoulnd't be able to move forward or backward
        if numPage == 1:
            forwardButton.undraw()
            backBut.undraw()
        elif page == 0:
            backBut.undraw()
        elif page == numPage:
            forwardButton.undraw()
        #detecting button press and updating bookmark
        backButton = self.backButton()
        while True:
            if forwardButton.onClick(True):
                book.setBookmark(book.getBookmark() + 1)
                self.win.resetMouse()
                for item in self.win.items[:]:
                    item.undraw()
                break
            if backBut.onClick(True):
                book.setBookmark(book.getBookmark() - 1)
                self.win.resetMouse()
                for item in self.win.items[:]:
                    item.undraw()
                break
            if backButton.onClick(True):
                for item in self.win.items[:]:
                    item.undraw()
                break

        return

    def displayPage(self, book):
        """ This method displays a single page at a time (375 chars) """
        bookContents = book.getText()
        bookLinesList = bookContents.split("\n")
        numLines = len(bookLinesList)
        numPages = numLines // self.pageLength  # calculate total number of pages in book
        while True:
            page = book.getBookmark()               # get current page (most recently read)
            pageStart = page * self.pageLength
            pageEnd = pageStart + self.pageLength   # display 20 lines per page
            if pageEnd > numLines:
                pageEnd = numLines                  # in case you're at the end of the book
            pageText = ""
            for i in range(pageStart, pageEnd):
                pageText += bookLinesList[i] + "\n"
            if numPages == 1:                       # alter page numbers for 1-page books
                page = 1
            pageNum = "Page %d out of %d" % (page, numPages)
            bookText = Text(Point(self.width * 0.5, self.height * 0.5), pageText)
            numText = Text(Point(self.width * 0.5, self.height * 0.95), pageNum)
            if self.width == 375: #text size adjustment for screen size
                bookText.setSize(self.textSize)
                numText.setSize(10)

            elif self.width == 450:
                bookText.setSize(self.textSize)
                numText.setSize(11)
            else:
                bookText.setSize(self.textSize)
                numText.setSize(14)

            bookText.draw(self.win)
            numText.draw(self.win)
            self.changePage(page, numPages, book)
            if self.backButton().onClick(True):
                for item in self.win.items[:]:
                    item.undraw()
                return
    def getWin(self):
        """Returns the window of the swindle"""
        return self.win

    def getOwned(self):
        """returns a list of buttons of all the books the owner owns"""
        bookButtons = []
        if len(self.ownedBooks) == 0:
            text = Text(Point(self.width * 0.5, self.height * 0.5), "You don't own any books")
            text.draw(self.win)
        else:
            #creates a list of buttons that corresponds to each books
            bookButtons = []
            x = 0.05
            for index in range(len(self.ownedBooks)):
                height = 1 / len(self.ownedBooks) 
                y = x + height/2 #x and y are calculated based on amount of books left
                buttonRect = Rectangle(Point(self.width*0.1, self.height * x), Point(self.width*0.9, self.height * y))
                bookButtons.append(Button(buttonRect, self.ownedBooks[index].toString(), self.win))
                x += height
        for book in bookButtons:
            if self.width == 375: #text size adjustment for screen size
                book.setSize(10)
            elif self.width == 450:
                book.setSize(11)
            else:
                book.setSize(14)
            book.draw()
        return bookButtons

    def showOwned(self):
        """prints all the books that the owner owns"""
        books = self.getOwned()
        backButton = self.backButton()
        while True:
            if backButton.onClick(True):
                for item in self.win.items[:]:
                    item.undraw()
                self.win.resetMouse()
                return

    
    def showAvailable(self):
        """show available books to be bought"""
        if len(self.availableBooks) == 0:
            text = Text(Point(self.width * 0.5, self.height * 0.5), "No books available")
            text.draw(self.win)
            return []
        else:
            #creates a list of buttons that corresponds to each books
            bookButtons = []
            x = 0.05
            for index in range(len(self.availableBooks)):
                height = 1 / len(self.availableBooks) 
                y = x + height/2 #x and y are calculated based on amount of books left
                buttonRect = Rectangle(Point(self.width*0.1, self.height * x), Point(self.width*0.9, self.height * y))
                bookButtons.append(Button(buttonRect, self.availableBooks[index].toString(), self.win))
                x += height
        for book in bookButtons:
            if self.width == 375: #text size adjustment for screen size
                book.setSize(10)
            elif self.width == 450:
                book.setSize(11)
            else:
                book.setSize(11)
            book.draw()
        
        return bookButtons
    
    def getOwner(self):
        return self.owner
        
    def getBooks(self):
        """returns list of all books"""
        allBooks = self.ownedBooks + self.availableBooks
        booksInfo = []
        for book in allBooks:
            bookInfo = []
            if book in self.availableBooks:
                bookInfo.append("available")
            else:
                bookInfo.append("owned")
            bookInfo.append(book.getTitle())
            bookInfo.append(book.getAuthor())
            bookInfo.append(book.getYear())
            bookInfo.append(book.getFilename())
            bookInfo.append(book.getBookmark())
            booksInfo.append(bookInfo)
        return booksInfo

    def buy(self):
        """allows user to buy book from available books"""
        bookButtons = self.showAvailable()
        #draw back buttons
        backButton = self.backButton()
        while True:
            if backButton.onClick(True):
                for item in self.win.items[:]:
                    item.undraw()
                break
            if len(bookButtons) >= 1:
                for index in range (len(bookButtons)):
                    #check if a buttons is clicked
                    if bookButtons[index].onClick(True):
                        ownedBook = self.availableBooks.pop(index)
                        #add to owned books
                        self.ownedBooks.append(ownedBook)
                        for book in bookButtons:
                            book.undraw()
                        #redraw options
                        bookButtons = self.showAvailable()
                        self.win.resetMouse()
                        break

    def backButton(self):
        """draws the button that allows the user to move back a page"""        
        backCirc = Circle(Point(self.width * 0.05, self.height * 0.1), self.width * 0.03)
        backButton = Button(backCirc, "🠔", self.win)
        backButton.draw()
        return backButton

    def read(self):
        """allows the user to read a book"""
        bookButtons = self.getOwned()
        backButton = self.backButton()
        while True:
            if backButton.onClick(True):
                for item in self.win.items[:]:
                    item.undraw()
                break
            for index in range (len(bookButtons)):
                #check if a buttons is clicked
                if bookButtons[index].onClick(True):
                    for item in self.win.items[:]:
                        item.undraw()
                    self.displayPage(self.ownedBooks[index])
                    bookButtons = self.getOwned()
        return
                    

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

