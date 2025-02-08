#Write a function that accepts string from user and print all permutations of that string.
global res 
res = set({})

def all_permutatons(str, fix = ''):
    if len(str) == 0:
        res.add(fix)
        return 
    
    for let in range(0, len(str)):
        cur = str[let]
        rem = str[:let] + str[let+1:]
        all_permutatons(rem, fix+cur)
        


str = input("Enter the String: ")
print("All permutations of that string: ")
all_permutatons(str)
for x in res:
    print(x)