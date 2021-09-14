"""
    Description: This program remove a user specified character from a given word.
    Name: Kenneth
    Date: Fall 2021
"""
def getChar():
    """
    Purpose: validates the user inputted character to make sure it is only one 
    Parameters: None
    Return Val: single length character
    """
    char = input("ch    :")
    while len(char) > 1:
        print("Invalid. Please enter a single character")
        char = input("ch    :")
    
    return char

def removeChar(string, char):
    """
    Purpose: Removes specified character from string
    Parametes: Base string(str), character to remove(str)
    Return Val: Final string with character removed
    """
    if len(string) == 0:
        return ""
    else:
        if string[-1] != char:
            return removeChar(string[0:-1], char) + string[-1] 
        return  removeChar(string[0:-1], char)

def main():
    string = input("string: ")
    char = getChar()
    print(removeChar(string, char) )

main()