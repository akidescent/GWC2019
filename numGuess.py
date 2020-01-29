#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20) #set variable aRandomNumber to random integer (1-20)
#can initialize any variable

# For Testing: print(aRandomNumber)

numGuesses = 0

while True: #set a forever loop
	guess = input("You have 20 tries. Guess a number between 1 and 20 (inclusive): ") #getting user input, a string

	if not guess.isnumeric(): # checks if a string is only digits 0 to 9
		print("That's not a positive whole number, try again!")
		continue
	else:
		guess = int(guess)
		numGuesses += 1
	if aRandomNumber == guess:
		print("Congradulations, you guessed the right number!")
		print(aRandomNumber)
		break



	elif (aRandomNumber < guess):
		print("Sorry your guess is too high, that's not it.")
	elif (aRandomNumber > guess):
		print("Sorry your guess is too low, that's not it.")

	if numGuesses >= 20: #number of tries >=2
		print("Sorry, you ran out of tries.")
		break
