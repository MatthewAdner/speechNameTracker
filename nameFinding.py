# this program checks the text file

# import name list from csv
import re

nameList = ['matthew','adam','lauren','jared']

calledList = {}
for name in nameList:
    calledList[name]=0

def gotWord(currentWord):
    #currentWord='adam'

    print(calledList)

    if currentWord.lower() in calledList:
        calledList[currentWord.lower()]+=1

    print(calledList)



sentence = "Hi Matthew, hi adam, hi jared lauren, hi JarED. adam adam matthew Lauren Lauren Lauren Lauren"

# got this code from https://stackoverflow.com/questions/6181763/converting-a-string-to-a-list-of-words
# I don't really know how it works, but it does.
wordList = re.sub("[^\w]", " ",  sentence).split()


for word in wordList:
    gotWord(word)