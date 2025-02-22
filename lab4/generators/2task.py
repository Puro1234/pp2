res = [] 
def evens(n):
    for i in range(n+1):
        if i%2 == 0:
            yield i

num = int(input("Enter a number: "))
for x in evens(num):
    res.append(str(x))

print(", ".join(res))