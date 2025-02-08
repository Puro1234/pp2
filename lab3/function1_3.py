#Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
#
def howManyRabbitsAndChickens(heads, legs):
    rabs = int((legs - (heads * 2))/2)
    chks = int(heads - rabs)
    print("It's", rabs, "rabbits", "and", chks, "chickens")

h = int(input("Heads: "))
l = int(input("Legs: "))
howManyRabbitsAndChickens(h, l)