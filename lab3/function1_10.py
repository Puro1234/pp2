#Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.

def uniqueList(listIn):
    resList = []
    for x in listIn:
        if x in resList:
            continue
        else:
            resList.append(x)
    return resList

listIn = list(input("Enter list's elements separated by spaces: ").split())
print("No dublicates version: ", *uniqueList(listIn))