#!/usr/bin/env python3

import random
import os


tries = 1
maxtries = 15
triesleft = 15

uname = input("Hello, What is your username?\n: ")

if uname == "nick":
    print("download pycharm!")
if uname == "Hello":
    print("That is a weird name")
if uname == "cheats":
    tries += 430
if uname == "":
    print("Fine don't tell me your name.")
if uname == "cheese":
    print("*camera shutter*")
if uname == "Destro":
    print("You did it!",uname,"wins! The number was not even made yet, and it only took 0 tries!")
    win = input("Press enter to close")
    if win == "":
        exit()
    else:
        exit()
if uname == "asdf":
    print("You should be more creative...")

diff = input("Choose Difficulty: easy, medium, hard, or expert\n: ")
if diff == "easy":
    print("Easy Mode Enabled")
    number = random.randint(1,50)
    maxtries = 20
    triesleft = 19
    if uname == "DEV":
        print("The secret number is:",number,".")
if diff == "medium":
    print("Medium Mode Enabled")
    number = random.randint(1,100)
    maxtries = 15
    triesleft = 14
    if uname == "DEV":
        print("The secret number is:",number,".")
if diff == "hard":
    print("Hard Mode Enabled")
    number = random.randint(1,1000)
    maxtries = 10
    triesleft = 9
    if uname == "DEV":
        print("The secret number is:",number,".")
if diff == "expert":
    print("Expert Mode Enabled")
    number = random.randint(1,10000)
    maxtries = 8
    triesleft = 7
    if uname == "DEV":
        print("The secret number is:",number,".")
if diff == "":
    print("Easy Mode Enabled")
    number = random.randint(1,50)
    maxtries = 20
    triesleft = 19
    if uname == "DEV":
        print("The secret number is:",number,".")
        
print("Hello", uname + ".", )

#do you want to play the game
question = input("Would you like to start the game? [Y/N]\n: ")
if question == "n":
    print("Too bad!")
    okay = input("Press enter to continue")
    if okay == "":
        question = "y"
    else:
        question = "y"
if question != "y" or "n":
    question = "y"

if question == "y":
    os.system('cls')
    if uname == "DEV":
        print("The secret number is:",number,"")
    if diff == "easy":
        print("I'm thinking of a number between 1 & 50")
        print("You have ",maxtries," tries")
    if diff == "medium":
        print("I'm thinking of a number between 1 & 100")
        print("You have ",maxtries," tries")
    if diff == "hard":
        print("I'm thinking of a number between 1 & 1,000")
        print("You have ",maxtries," tries")
    if diff == "expert":
        print("I'm thinking of a number between 1 & 10,000")
        print("You have ",maxtries," tries")
    #guess

    try:
        guess = int(input("Have a guess: "))
    except:
        guess = int(input("Please only use integers: "))
    if uname == "luckyy":
        number = guess


    if guess > number:
        print("Guess lower...")
if guess < number:
    print("Guess higher...")
#tries
while guess != number:
    tries += 1
    if tries + 1:
        triesleft -= 1
    print("You have ",triesleft," tries left")
    if tries == maxtries:
        print("You used up all of your tries! The number was",number,".")
        gameover = input("Press enter to exit")
        if gameover == (""):
            exit()
        else:
            exit()
    try:
        guess = int(input("Try again: "))
    except:
        guess = int(input("Try again, numbers only: "))

    if guess < number:
        print("Guess higher")
    if guess > number:
        print("Guess lower")
#Ending
if guess == number:
    print("Your're right!",uname,"wins! The number was", number,",")
    if tries > 1:
        print("and it only took you",tries,"tries!")
    if tries <= 1:
        print("and it only took you",tries,"try!")
        print("Wow that was lucky! Or you're cheating!")
    if tries >= 8:
        print("Took you long enough!")
leave = input("This game was made by Nicholaus Whites!\nPress enter to exit.\n: ")
if leave == "y":
    exit(222)
else:
    exit(111)
