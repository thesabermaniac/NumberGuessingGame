import random
num = random.randrange(1,101)
loop = True
while loop:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == num:
        print("You Got It!")
        loop = False
    elif guess > 100 or guess < 1:
        print('Learn how to read you fool')
    elif guess < num:
        print("Too low")
    else:
        print("Too high")
