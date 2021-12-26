"""
    Description: Gui for ereader programs
    Author: Kenneth
    Date: Fall 2021
"""
from tkinter.constants import ON
from typing import Type
from graphics import *
from enhancedSwindle import *
from slider import *
from button import *
from os.path import isfile

def getWinSize(width, height, win):
    """allows first time users to select the size of their ereader window"""
    sizeText = "Choose Window Size (cannot be changed)"
    text = Text(Point(width * 0.5, height * 0.1), sizeText)
    p1 = Point(width * 0.4, height * 0.3)
    p2 = Point(width * 0.6, height * 0.4)

    rectButtonS = Rectangle(p1, p2)
    rectButtonM = rectButtonS.clone()
    rectButtonM.move(0, height * 0.2)
    rectButtonL = rectButtonM.clone()
    rectButtonL.move(0, height * 0.2)

    smallButton = Button(rectButtonS, "300 x 400", win) 
    medButton = Button(rectButtonM, "384 x 512", win)
    largeButton = Button(rectButtonL, "480 x 640", win)

    text.setSize(16)
    text.draw(win)
    smallButton.draw()
    medButton.draw()
    largeButton.draw()

    #detect the mouse click for each of the options
    size = None
    while size == None:
        if smallButton.onClick([300, 400]) ==  [300,400]:
            size = [300,400]
        elif medButton.onClick([384,512]) ==  [384,512]:
            size = [384,512]
        elif largeButton.onClick([480, 640]) == [480, 640]:
            size = [480, 640]
    win.close()
    return size

def newUser():
    width = 500
    height = 600
    firstTimeWin = GraphWin("First Time Launch", width, height)

    #draw all the text stuff
    topText = "Since this is the first time you used it,"
    midText = "let's customize your Swindle..."
    botText = "Please enter your name: "
    welcomeTextTop = Text(Point(width * 0.5, height * 0.25), topText)
    welcomeTextMid = Text(Point(width * 0.5, height * 0.3), midText)
    welcomeTextBot = Text(Point(width * 0.2, height * 0.46), botText)
    nameEntry = Entry(Point(width * 0.5, height * 0.5), int(width * 0.1))
    buttonShape = Rectangle(Point(width * 0.4, height * 0.6), (Point(width * 0.6, height * 0.65)))
    nextButton = Button(buttonShape, "Next", firstTimeWin)
    welcomeTextTop.setSize(20)
    welcomeTextTop.setSize(14)
    welcomeTextBot.setSize(12)

    welcomeTextBot.draw(firstTimeWin)
    nameEntry.draw(firstTimeWin)
    welcomeTextTop.draw(firstTimeWin)
    welcomeTextMid.draw(firstTimeWin)
    nextButton.draw()

    #get owned from text box with either a click or a enter
    owner = None
    while owner == None:
        CLICK = nextButton.onClick(True)
        if firstTimeWin.checkKey() == "Return" or CLICK:
            if nameEntry.getText != "":
                owner = nameEntry.getText()
    welcomeTextBot.undraw()
    nameEntry.undraw()
    welcomeTextTop.undraw()
    welcomeTextMid.undraw()
    nextButton.undraw()
    size = getWinSize(width, height, firstTimeWin)
    return owner, size

def saveUser(swindle):
    """saves user preferences to a file"""
    owner = swindle.getOwner()
    books = swindle.getBooks()

    outfile = open("user-settings.txt", "w")
    outfile.write("%s\n" %owner)
    for book in books:
        book = str(book)
        book = book.strip("[]")
        book = book.replace("'", "")
        outfile.write("%s\n" %book)
    outfile.close()

def loadUser():
    """loads in already save user preferences from user-settings.txt"""
    owner = ""
    availableBooks = []
    ownedBooks = []
    
    infile = open("user-settings.txt")
    lineCount = 1
    for line in infile:
        if lineCount == 1:
            owner = line.strip() #gets the owner
        else:
            line = line.strip()
            line = line.split(", ")
            if line[0] == "owned":
                #create book with preset settings
                ownedBook = Book(line[1], line[2], line[3], line[4])
                ownedBook.setBookmark(int(line[5])) #add bookmark
                ownedBooks.append(ownedBook)
            if line[0] == "available":
                #do the same thing for availaible books
                availableBooks.append(Book(line[1], line[2], line[3], line[4]))
        lineCount += 1
    #create swindle with user settings
    userSwindle = Swindle(owner, ownedBooks, availableBooks)
    print("\nWelcome to %s's Swindle v1.0!" % owner)
    infile.close()
    return userSwindle

def mainMenu(win):
    width = win.getWidth()
    height = win.getHeight()
    #load all the options as buttons
    buyRect = Rectangle(Point(width * 0.1, height * 0.1), Point(width * 0.9, height * 0.25))
    ownedRect = buyRect.clone()
    ownedRect.move(0, height * 0.2)
    readRect = ownedRect.clone()
    readRect.move(0, height * 0.2) 
    exitRect = readRect.clone()
    exitRect.move(0, height *0.2)

    buyButton = Button(buyRect, "Buy/See Available Books", win)
    ownedButton = Button(ownedRect, "See Owned Books", win)
    readButton = Button(readRect, "Read a Book", win)
    exitButton = Button(exitRect, "Exit", win)

    buyButton.draw()
    ownedButton.draw()
    readButton.draw()
    exitButton.draw()

    #dectect mouse click for each of the options
    choice = None
    while choice == None:
        if buyButton.onClick(True):
            choice = 1
        elif ownedButton.onClick(True):
            choice = 2
        elif readButton.onClick(True):
            choice = 3
        elif exitButton.onClick(True):
            choice = 4
    for item in win.items[:]:
        item.undraw()
    win.flush()
    win.resetMouse()
    return choice

def main():
    if isfile("user-settings.txt"): #checks if it is first time using 
        userSwindle = loadUser()
    else:
        owner, size = newUser()                   # Display instructions and get user's name
        ereaderWin = GraphWin("%s's Swindle" %owner, size[0], size[1])
        userSwindle = Swindle(owner, [], [], ereaderWin)        # Create a new Swindle ereader for them
          
    while True:
        menuChoice = mainMenu(ereaderWin)         # Display ereader's main menu
        if menuChoice == 1:
            userSwindle.buy()           # View available books with option to buy
        elif menuChoice == 2:
            userSwindle.showOwned()     # View owned books
        elif menuChoice == 3:
            userSwindle.read()          # Choose a book to read
        else:
            break                       # Turn off ereader (quit the program)
        print(menuChoice)
    # saveUser(userSwindle)


main()

