def main():
    number = int(input("enter a non negative integer:"))
    fact = factorial(number)
    print("the factorial of num is :",fact)

def factorial(num):
    if num == 0:
        return 1
    else :
        return num * factorial(num - 1)
main()