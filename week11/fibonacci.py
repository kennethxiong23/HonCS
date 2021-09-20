"""hahah funy fibbinoccii"""
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        newNum = fibonacci(num-1) + fibonacci(num-2)
        
        return fibonacci(num-1) + fibonacci(num-2)

def main():
    num = int(input("Give me a int"))
    print(fibonacci(num))

main()