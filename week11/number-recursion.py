def blastoff_iterative(n):
    """ This function uses iteration to display a countdown from a number (n)
        to 1 and print "blastoff" when it gets to 0. """
    for i in range(n, 0, -1):
        print(i)
    print("blastoff!")


def blastoff_recursive(n):
    """ This function uses recursion to display a countdown from a number (n)
        to 1 and print "blastoff" when it gets to 0. """

    if n <= 0:
        print("blastoff")
    else:
        print(n)
        blastoff_recursive(n-1)



def sumN_iterative(n):
    """ Function to return the sum from 1 to a number using iteration """
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


def sumN_recursive(n):
    """ Function to return the sum from 1 to a number using recursion """
    if n <= 0:
       return 0
    else:
        sum = n + sumN_recursive(n-1)
    return sum


def main():

    n = int(input("Enter a value for n: "))
    blastoff_iterative(n)
    blastoff_recursive(n)

    n = int(input("Enter a value for n: "))
    print(sumN_iterative(n))
    print(sumN_recursive(n))


main()
