class Book(object):
    """ class for a single Book object """

    def __init__(self, title, author, year, filename):
        """ constructor for book object, given title(str), author(str), year(int), filename(str)
        """
        self.title = title
        self.year = year
        self.author = author
        self.filename = filename
        self.bookmark = 0

    def toString (self):
        """ pretty-print info about this object """
        return "%25sby %20s(%s)" %(self.title, self.author, self.year)

    def getTitle(self):
        "returns the title"
        return self.title
    
    def getAuthor(self):
        "returns the author"
        return self.author

    def getFilename(self):
        "returns the filename"
        return self.filename

    def getYear(self):
        "returns the year"
        return self.year
    
    def getBookmark(self):
        "returns the bookmark spot"
        return self.bookmark
    
    def setBookmark(self, bookmark):
        "set bookmark spot"
        self.bookmark = bookmark

    def getText(self):
        "get the text"
        readFile = open(self.filename, "r")
        text = ""
        for line in readFile:
            if line[0] != "#":
                line = line.strip()
                text = text + line + "\n"
        return text


if __name__ == '__main__':

    print("Testing the Book class...")
    myBook = Book("Gettysburg Address", "Abe Lincoln", 1863,
    "book-database/gettysburg.txt")

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

    ################ Write additional tests below ###################
