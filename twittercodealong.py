import json

tweetFile = open("tweets_small.json", "r")

tweetData = json.load(tweetFile)

tweetFile.close()
#
# print("Tweet ID: ", tweetData[0]["id"])
#
# print("Tweet text: ", tweetData[0]["text"])

#for each index, of the overall list
for i in range(len(tweetData)):
    print("Tweet text: " + tweetData[i]["text"])
#now in tweet data
for tweet in tweetData:
    print("Tweet Text: " + tweet["text"])

# print("name: ", tweetData[0]["name"])
