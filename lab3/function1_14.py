#Create a python file and import some of the functions from the above 13 tasks and try to use them.
from functions1_13 import game

print("Do you wanna play a game? yes/no")
answ = input()
if answ == "yes":
    game()
else:
    print("I don't care actually, you have to play anyways")
    game()