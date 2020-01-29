from random import *

aRandomNumber = randint(1, 20)
for i in range(5):
    print(i)

#set a forever loop
    guess = input("You have 5 tries. Guess a number between 1 and 20 (inclusive): ") #getting user input, a string

    if not guess.isnumeric(): # checks if a string is only digits 0 to 9
    	print("That's not a positive whole number, try again!")
    	continue

    else:
    	guess = int(guess)

    if aRandomNumber == guess:
    	print("Congradulations, you guessed the right number!")
    	print(aRandomNumber)
    	break



    elif (aRandomNumber < guess):
    	print("Sorry your guess is too high, that's not it.")
    elif (aRandomNumber > guess):
    	print("Sorry your guess is too low, that's not it.")


    #same, dont keep numGuesses though
