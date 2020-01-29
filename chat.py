from random import *
# --- Define your functions below! ---
def begin():
    print("Hi! I'm Chatbot. I love talking to people!")

def name():
    print("What is your name?")
    user_input = input()
    print("Hello " + user_input + "! Nice to meet you!")
    return user_input

def color():
    print("What's your favorite color?")
    userColor = input()
    print(userColor + " is my favorite too!")

def respond(answer, user_input):
    res = ["hi" + user_input , "hello", "howdy"," hey", "greetings"]
    res2 = ["tell me a joke", "make a funny", "make me laugh", "lol", "be funny"]
    res3 = ["owo", "uwu", "memes", "send memes", "meme", "me me"]

    GreetRes = ["'sup bro", "hey", "what's good fam", "*nods*", "hi to you too!"]
    GreetRes2 = ["my life", "memes", "uwu", "captialism", "communism"]

    numres = ["tell me a number", "number", "give number", "give me a number"]
    aRandomNumber = randint(1, 999)
    aRandomIndex = randint(0, len(GreetRes)-1)
    aRandomIndex = randint(0, len(GreetRes2)-1)

    if answer in res:
        print ("\n" + GreetRes[aRandomIndex])
    elif answer in res2:
        print("\n" + GreetRes2[aRandomIndex])
    elif answer in res3:
        print("\n" + "owo!!!" + "\n")
    elif answer in numres:
        print(aRandomNumber)


def default():
    print("\n" + "Cool! Keep talking, I'm listening..." + "\n")

def processInput(answer):
    if answer == "hi":
        sayGreeting

# --- Put your main program below! ---
def main():
    begin()
    user_input = name()
    color()

    while True:
        answer = input("Reply: ")
        respond(answer, user_input)

        default()


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
