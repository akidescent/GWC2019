import json

list_of_answers = []

questions =
[
    "What is your name?",
    "What's your favorite color?",
    "When were you born?",
    "Do you have a pet?",
    "What city do you live in?",
    "What phone app or website are you on most often?"
]

keys = ["name", "color", "birth", "pet", "city", "website"]
done = "NO"
while done == "NO":

    answers = {}

    for i in range(len(questions)):
        answer = input(questions[i] + ": ")
        answers[keys[i]] = answer

    list_of_answers.append(answers)

    done = input("Are you done collecting info? Type 'yes' or 'no'  ").upper()

print(list_of_answers)

print("Thank you for your response(s).")

f = open("allanswers.json", "r")
olddata = json.load(f)
list_of_answers.extend(olddata)
f.close()

f = open("allanswers.json", "w")
f.write('[\n')
index = 0
for t in list_of_answers:
    if index < (len(list_of_answers) - 1):
        json.dump(t, f)
        f.write(',\n')
    else:
        json.dump(t, f)
        f.write('\n')
    index += 1

f.write(']')
f.close()

names = []

for s in range(len(list_of_answers)):
    names.append(list_of_answers[s]["name"])

print(names)

# this works but first way easier syntax

# answers2 = {}
# answer = input("What is your name?: ")
# answers2["name"] = answer
# answer = input("What is your fav color?: ")
# answers2["color"] = answer
# answer = input("What is your birthday?: ")
# answers2["birth"] = answer
# answer = input("Do you have a pet?: ")
# answers2["pet"] = answers
#
# print()
# print (answers2)
