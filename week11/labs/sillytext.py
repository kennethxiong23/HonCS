"""
    Description: This program asks the user for a word and a number. It then repeats every
                         character in the word that number of times.
    Name: Kenneth
    Date: Fall 2021
"""
def repeatChar(string, num):
    """
    Purpose: Recursive function that repeats each char in the string a given number of times
    Parameters: Starting string(str), number of times each char is repeated(int)
    Return Val: final string with multiplied characters
    """
    if len(string) == 0:
        return ""
    else:
        return string[-1] * num + repeatChar(string[0:-1], num)
        
def main():
    string = input("string: ")
    number = int(input("num: "))
    print("\n" + repeatChar(string, number))

main()