#import sounddevice as sd
 
from os import times
import speech_recognition as sr
import re
import matplotlib.pyplot as plt

# list of availible microphones
mLis = sr.Microphone.list_microphone_names()

# chooses a mic to listen to
mic = sr.Microphone(device_index=1)#mLis.index('Microphone (Logitech Mic (Commu'))
print(sr.Microphone.list_microphone_names())

# list of names
nameList = ['matthew', 'adam', 'lauren', 'jared', 'jason']


# creates dictionaries for the names
googleCalledDict = {}
#sphinxCalledDict = {}
for name in nameList:
    googleCalledDict[name]=0
#    sphinxCalledDict[name]=0

#i tried to make a figure that would update but the figure doesn't show u with axis so I gave up
'''fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
students = googleCalledDict.keys()
timesCalled = googleCalledDict.values()
ax.bar(students,timesCalled)
plt.show()'''

# function to check for a word in a string
def gotName(sentence, calledDict):
    
    wordList = re.sub("[^\w]", " ",  sentence).split()
    for word in wordList:
        if word.lower() in calledDict:
            calledDict[word.lower()]+=1




r = sr.Recognizer()

with mic as source:
    while True:
        try:
            audio=r.listen(source)
            
            '''print('sphinx:')
            spinxTemp = r.recognize_sphinx(audio)
            gotName(spinxTemp, sphinxCalledDict)
            print(spinxTemp)
            print(sphinxCalledDict)'''

            googleTemp = r.recognize_google(audio) # returns a string of what the speech recognition things was said
            print('google:')
            gotName(googleTemp, googleCalledDict)
            print(googleTemp)
            print(googleCalledDict)

        # allows the program to exit when ctrl+c
        except KeyboardInterrupt:
            exit('You interrupted through the keyboard.')

        # sometimes theres an error, maybe if it can't understand what it hears
        except:
            print('There was a problem.')

