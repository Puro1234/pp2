#Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
#Hello! What is your name?
#KBTU
#
#Well, KBTU, I am thinking of a number between 1 and 20.
#Take a guess.
#12
#
#Your guess is too low.
#Take a guess.
#16
#
#Your guess is too low.
#Take a guess.
#19
#
#Good job, KBTU! You guessed my number in 3 guesses!
import random

def game():
    print("Hello! What is your name?")
    name = input()
    print()
    print("Well,", name + ", I am thinking of a number between 1 and 20.")
    ran = random.randint(1, 20)
    cnt = 0
    while(True):
        print("Take a guess.")
        guess = int(input())
        cnt += 1
        print()
        if (guess == ran):
            break
        elif(guess < ran):
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
    print("Good job, " + name + "! You guessed my number in", cnt, "guesses!")


game()