import random

# A list of words that
potential_words = ["example", "words", "someone", "can", "guess"]
#choosing random word
word = random.choice(potential_words)

# Use to test your code:
# print(word)

# Converts the word to lowercase, standardizes the word
word = word.lower()

# Make it a list of letters for someone to guess
current_word = ""

for letter in word:

    current_word = current_word + "_" # TIP: the number of letters should match the word

# for i in range(len(word)) #[same thing]
#     current_word = current_word + "_" # TIP: the number of letters should match the word

print(current_word)


# Some useful variables
guesses = []
maxfails = 7
fails = 0

while fails < maxfails: #needs a boolean conditional
	guess = input("Guess a letter: ")

    #guess = str(guess)
        # check if the guess is valid: Is it one letter? Have they already guessed it?
    if guess in guesses:
        print("You have already guessed that letter, try again.")
        continue
    if len(guess) != 1:
        print("Please only enter 1 letter, try again.")
        continue #starts from the top


	# check if the guess is correct: Is it in the word? If so, reveal the letters!
    if guess in word:
        guesses.append(guess)
        for i in range(len(word)):
            if word[i] == guess:
                current_word[i] = guess
    if "_" not in current_word:
        print("YOU WIN?!")
        break

	#print(current_word)
#
	   fails = fails + 1
	   print("You have " + str(maxfails - fails) + " tries left!")
