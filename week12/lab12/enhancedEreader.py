from enhancedSwindle import *
from book import *
from os.path import isfile

def newUser():
    print("\nSince this is the first time you used it,")
    print("let's customize your Swindle...")
    owner = str(input("\nPlease enter your name: "))
    print("\nWelcome to %s's Swindle v1.0!" % owner)
    return owner

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
        owner = newUser()                   # Display instructions and get user's name
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
