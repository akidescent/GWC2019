#imports abiliy to get random number
from random import *

#creates a list
aList = ["Dorthey", "Aprile", "Cindy",]

#generates a random ineger
aRandomIndex = randint(0, len(aList)-1)

print(aList[aRandomIndex])

print(len(aList))

print("Cindy" in aList)

if "Cindy" in aList:
    print("Hello Cindy")

if "Amanda" not in aList:
    print("where is Amanda?")

#printing each letter of string on different lines 
for letter in aList[0]:
    print(letter)

#taking the first letter of each item in the list
for item in aList:
    print(item[0])
