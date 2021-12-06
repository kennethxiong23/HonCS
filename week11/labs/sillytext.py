"""
    Description: This program asks the user for a word and a number. It then 
                  repeats every character in the word that number of times.
    Author: Kenneth
    Date: Fall 2021
"""

def repeatChar(string, num):
    """
    Purpose: Recursive function that repeats each char in the string a given 
             number of times
    Parameters: Starting string(str), number of times each char is repeated(int)
    Return Val: final string with multiplied characters
    """
    if len(string) == 0:
        return ""
    else:
        returnStr = repeatChar(string[:-1], num) + string[-1] * num
        return returnStr

def getUserInput(prompt):
    """
    Purpose: Gets the user input for a number and makes sures it's a positive int.
    Parameters: prompt(str)
    Return Val: validated integer
    """
    while True:
        userInput = input(prompt)
        try:
            num = int(userInput)
            if 0 < num:
                return num
            else:
                print("invalid input, try again")
        except ValueError:
            print("invalid input, try again")
        
def main():
    string = input("string: ")
    prompt = "num: "
    number = getUserInput(prompt)
    print("\n" + repeatChar(string, number))


main()