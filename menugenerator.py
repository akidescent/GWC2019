from random import *

aSide = ["Green Beans", "Creamed Corn", "Roasted Carrots", "Sauteed Mushrooms", "Steamed Broccoli"]
aMain = ["Chicken and Lemon", "Shrimp Pasta", "Steak", "Tomato Pasta", "Veggie Fried Rice"]
aDessert = ["NY-style Cheesecake", "Strawberry Parfait", "Vanilla Ice Cream", "Cupcake with Sprinkles", "Chocolate Cake"]

aRandomIndex = randint(0, len(aSide)-1)
aRandomIndex = randint(0, len(aMain)-1)
aRandomIndex = randint(0, len(aDessert)-1)

while True:
    print("Randomly generating a menu...")
    print(" \n")

    print("Your side:")
    print(aSide[aRandomIndex])
    print(" \n")

    print("Your Main Dish:")
    print(aMain[aRandomIndex])
    print(" \n")

    print("Your Dessert:")
    print(aDessert[aRandomIndex])
    print(" \n")

    print("Do you like your menu? [y/n]")
    user_input = input()
    if user_input == "y":
        print("Enjoy your meal!")
        break
    elif user_input == "n":
        print("I'll try again...")
        exit()
