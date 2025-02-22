def squares(n):
    i = 1
    while(i <= n):
        yield i**2
        i += 1

num = int(input("Enter a number: "))
for x in squares(num):
    print(x)