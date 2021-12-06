"""
    Purpose: This program allows the user to search for filenames containing a 
             given pattern in a given directory.
    Author: Kenneth
    Date: Fall 2021
""" 
from os import listdir
from os.path import isdir, expanduser

def recursiveSearch(path, pattern):
    """
    Purpose: Recurisvely searches through directories
    Parameters: path(string), pattern to look for(string)
    Return Val: None
    """
    if isdir(path) == False:
        if pattern in path:
            print(path)
        return
    else:
        directories = listdir(path)
        homeDir = path
        for dir in directories:
            if path[-1] != "/":
                path = homeDir + "/%s" %dir
            else:
                path = homeDir + dir
            recursiveSearch(path, pattern)

def main():
    path = input("Path: ")
    pattern = input("Pattern: ")
    path = expanduser(path)
    if isdir(path):
       recursiveSearch(path, pattern)


main()
