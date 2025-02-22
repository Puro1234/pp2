def divisible_by_12(num):
    for i in range(0, num+1):
        if i%12 == 0:
            yield i

num = int(input("Enter a number: "))
for x in divisible_by_12(num):
    print(x)