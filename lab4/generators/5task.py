def allnums(n):
    i = n
    while(i >= 0):
        yield i
        i -= 1

num = int(input("Enter a number: "))

for x in allnums(num):
    print(x)