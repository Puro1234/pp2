def squares(a, b):
    i = a
    while(i <= b):
        yield i**2
        i += 1

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
for x in squares(a, b):
    print(x)