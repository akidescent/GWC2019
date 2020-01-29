
# Update this text to match your story.
start = '''
Join Space Dog on an Adventure! Choose your fate...
Red or Blue planet?
'''

print(start)

while True:
    print("Type 'r' to go to the Red Planet or 'b' to go to the Blue Planet.") # Update to match your story.
    user_input = input()
    if user_input == "r":
        print("You decided to go to the Red Planet...") # Update to match your story.
        print("Space Dog finds himself in a Jungle.")
        while True:
            print("Does Space Dog want to 'jump' or 'walk'?")
            user_input = input()
            if user_input == "jump":
                print("Space Dog jumps and says 'ok byeee...'")
                print("GAME ENDED.")
                break
                sys.exit([arg])
            elif user_input == "quit":
                        break
                        sys.exit([arg])

            elif user_input == "walk":
                print("Space Dog is walking...")
                print("Space Dog finds a Plant!")
                while True:
                    print("The plant is asking: do you want to 'eat' me, 'touch' me, or 'ignore' me?")
                    user_input = input()
                    if user_input == "eat":
                        print("Space Dog walks towards the plant, eats it, and then feels so sick that he disappears...")
                        print("Space Dog's adventure is over now...")
                        print("GAME ENDED.")
                        break
                        sys.exit([arg])
                    elif user_input == "touch":
                        print("Space Dog walks towards the plant, touches it, claims it hurt, makes a funny face, and disappears...")
                        print("Space Dog's adventure is over now...")
                        print("GAME ENDED.")
                        break
                        sys.exit([arg])
                    elif user_input == "ignore":
                        print("Space Dog turns to the left and leaves...")
                        print("Space Dog's adventure is over now...")
                        print("GAME ENDED.")
                        break
                        sys.exit([arg])


    elif user_input == "b":
        print("You decided to go to the Blue Planet...") # Update to match your story.
        print("Space Dog finds himself in a City.")
        while True:
            user_input = input()
            print("Does Space Dog want to 'jump' or 'walk'?")
            if user_input == "jump":
                print("Space Dog jumps and says 'ok byeee...'")
                print("GAME ENDED.")
                break
            elif user_input == "quit":
                    break
                    sys.exit([arg])

            elif user_input == "walk":
                print("Space Dog found a friend")
                while True:
                    print("Should he 'ignore' his new friend or 'befriend' him?")
                    user_input = input()
                    if user_input == "ignore":
                        print("Space Dog turns to the left and leaves...")
                        print("Space Dog's adventure is over now...")

                        break
                        break
                        sys.exit([arg])
                    elif user_input == "befriend":
                        print("Space Dog explores the City with his new Friend. He finds out that his new friend is named Ripley.")
                        print("GAME ENDED.")
                        break
                        sys.exit([arg])
