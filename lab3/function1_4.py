#You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.

def isXprime(x):
    if x < 2:
        return False
    for i in range(1, x):
        if i != 1 and x%i == 0:
            return False
    return True

def filter_prime(inputList):
    resList = []
    for x in inputList:
        if isXprime(int(x)):
            resList.append(x)
    return resList

listIn = list(input("Enter numbers separated by spaces: ").split())
print("Prime numbers: ")
for x in filter_prime(listIn):
    print (x)
