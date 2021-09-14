import math

def factorial_recursive(n):
    """ Function to return the factorial of a number using recursion """
    if n <= 1:
        return 1
    else:
        product = n * int(factorial_recursive(n-1))
    return product


def factorial_iterative(n):
    """ Function to return the factorial of a number using iteration """
    product = 1
    for i in range(1,n+1):
        product = product * i
    return product


def factorial_math_library(n):
    """ The math library's function to return the factorial of a number """
    product = math.factorial(n)
    return product


def main():

    n = int(input("Enter a value for n: "))

    print(factorial_iterative(n))
    print(factorial_recursive(n))
    print(factorial_math_library(n))


main()
