import random

# A list of words that
potential_words = ["example", "words", "someone", "can", "guess"]

word = random.choice(potential_words)

# Use to test your code:
#print(word)

# Converts the word to lowercase
word = word.lower()
guesses = []
maxfails = 7
fails = 0

# Make it a list of letters for someone to guess
if fails < 7:
	current_word = word
	print ("-" * len(current_word))




# 	word.appended("_")# TIP: the number of letters should match the word
# print(len(word))


# Some useful variables
guesses = []
maxfails = 7
fails = 0

while fails < maxfails:
	guess = input("Guess a letter: ")

	# check if the guess is valid: Is it one letter? Have they already guessed it?
	if letter in word
		#replace underscore with letters

	if letter not in word


	# check if the guess is correct: Is it in the word? If so, reveal the letters!



	fails = fails+1
	print("You have " + str(maxfails - fails) + " tries left!")
