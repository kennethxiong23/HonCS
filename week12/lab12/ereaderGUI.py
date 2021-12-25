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

    while width != 300 and width != 384 and width != 480:
        smallPressed = smallButton.onClick((300, 400))
        medPressed = medButton.onClick((384, 512))
        largePressed = largeButton.onClick((480, 640))
        if smallPressed != None or medPressed != None or largePressed != None:
            print ('ehy')

    win.close()
    print(width)
    return width, height 
    

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
    width, height = getWinSize(width, height, firstTimeWin)
    return owner, width, height, firstTimeWin


    # firstTimeWin.getMouse()
    # print("\nSince this is the first time you used it,")
    # print("let's customize your Swindle...")
    # owner = str(input("Please enter your name: "))
    # while owner == "":
    #     owner = input("Please enter a value: ")
    # print("\nWelcome to %s's Swindle v1.0!" % owner)
    return "bob", "bob", "bob", "bob"

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

def mainMenu():
    print("\n--------------------------------------------------\n")
    print("1) Buy/See available books\n2) See owned books\n3) Read a book\n4) Exit\n")
    while True:
        userInput = str(input("---> "))
        try:
            menuChoice = int(userInput)
            if 1 <= menuChoice <= 4:
                return menuChoice
            else:
                print("invalid number, try again")
        except ValueError:
            print("invalid input, try again")

def main():
    if isfile("user-settings.txt"): #checks if it is first time using 
        userSwindle = loadUser()
    else:
        owner, win, width, height = newUser()                   # Display instructions and get user's name
        userSwindle = Swindle(owner, [], [])        # Create a new Swindle ereader for them
          
    while True:
        menuChoice = mainMenu()         # Display ereader's main menu
        if menuChoice == 1:
            userSwindle.buy()           # View available books with option to buy
        elif menuChoice == 2:
            userSwindle.showOwned()     # View owned books
        elif menuChoice == 3:
            userSwindle.read()          # Choose a book to read
        else:
            break                       # Turn off ereader (quit the program)
    saveUser(userSwindle)


main()

