"""
programs looks for pattern in the given string
"""
def isPattern(pattern, text):
    for i in range (len(text)):
        if pattern == text[i: i +len(pattern)]:
            return i
    return "no"

def main():
    text = input("text: ")
    pattern = input("pattern: ")
    
    index =isPattern(pattern, text) 
    print(index)



main()