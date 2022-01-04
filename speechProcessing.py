#import sounddevice as sd
 
from os import times
import speech_recognition as sr
import re
import matplotlib.pyplot as plt

# list of availible microphones
mLis = sr.Microphone.list_microphone_names()

# varaible containing which device is being listened through.
dIndex = 1


# chooses a mic to listen to
mic = sr.Microphone(device_index=dIndex)#mLis.index('Microphone (Logitech Mic (Commu'))
#print(sr.Microphone.list_microphone_names())

q=str(input("print the list of mics? (y/n)"))
if q.lower()=='y':
    print(sr.Microphone.list_microphone_names())

print(sr.Microphone.list_microphone_names()[dIndex])

# list of names
nameList = ['matthew', 'adam', 'lauren', 'jared', 'jason']


# creates dictionaries for the names
googleCalledDict = {}
#sphinxCalledDict = {}#
for name in nameList:   
    googleCalledDict[name]=0
    #sphinxCalledDict[name]=0#
    

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
import matplotlib.pyplot as plt#; plt.rcdefaults()
#import numpy as np
import matplotlib.pyplot as plt

students = nameList#['Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp']
#y_pos = objects# = np.arange(len(objects))
timesCalled = [googleCalledDict[nameList[0]],googleCalledDict[nameList[1]],googleCalledDict[nameList[2]],googleCalledDict[nameList[3]],googleCalledDict[nameList[4]]]

plt.bar(students, timesCalled, align='center')#, alpha=0.5)
plt.xticks(students, students)
plt.ylabel('Times Said')
plt.xlabel('Student Names')
plt.title('Title')

plt.show()
with mic as source:
    while True:
        try:
            print('iran')
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

