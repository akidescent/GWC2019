#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
aName = ["Mary", "Patricia", "Jennifer", " Linda", "Elizabeth", "Barbara", "Susan", "Karen", "Nancy", "Margaret", "Lisa", "Betty", "Dorothy", "Sandra", "Ashley", "Kimberly", "Donna", "Emily", "Michelle", "Carol", "Amanda", "Melissa", "Deborah", "Stephanie"]

#Generates a random integer.
aRandomIndex = randint(0, len(aName)-1)

#name generator
print("Randomly generate a name from the top 25 popular female names!")
print(aRandomIndex)
print(aName[aRandomIndex])
