class Book(object):
    """ class for a single Book object """

    def __init__(self, title, author, year, filename):
        """ constructor for book object, given title(str), author(str), year(int), filename(str)
        """
        self.title = title
        #year book was published
        self.year = year
        self.author = author
        #variable for the path of the file
        self.filename = filename
        self.bookmark = 0

    def toString (self):
        """ pretty-print info about this object """
        return "%25sby %20s(%s)" % (self.title, self.author, self.year)

    def getTitle(self):
        return self.title
    
    def getAuthor(self):
        return self.author

    def getFilename(self):
        return self.filename

    def getYear(self):
        return self.year
    
    def getBookmark(self):
        return self.bookmark
    
    def setBookmark(self, bookmark):
        self.bookmark = bookmark

    def getText(self):
        inFile = open(self.filename, "r")
        fullText = ""
        for line in inFile:
            if line[0] != "#":
                text = line.strip()              
                fullText = fullText + text + "\n"
        inFile.close()
        return fullText


if __name__ == '__main__':

    print("Testing the Book class...")
    # myBook = Book("Gettysburg Address", "Abe Lincoln", 1863,
    # "book-database/gettysburg.txt")
    myBook = Book("Alice in wonderland", "persn", 1862,
    "book-database/alice.txt")
    

    print("Testing toString...")
    print(myBook.toString())

    print("Testing getFilename...")
    print(myBook.getFilename())

    print("Testing getText...")
    text = myBook.getText()
    print(text[:105])                   # only print the first couple of lines

    print("bookmark is:", myBook.getBookmark())
    myBook.setBookmark(12)
    print("now bookmark is:", myBook.getBookmark())
    print("title", myBook.getTitle())
    print("year", myBook.getYear())
    print("filename", myBook.getFilename())
    print("author", myBook.getAuthor())

   