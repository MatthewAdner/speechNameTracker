#import sounddevice as sd

import os
import matplotlib
from matplotlib import animation
from numpy.core.shape_base import block
import speech_recognition as sr
import re
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import date, datetime

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

startTime = str(datetime.now())
filePath ='C:/Users/matth/codeProjects/speechNameTracker/transcripts/'
fileName = 'audioNameStream_'+str(startTime)+'secs.txt'
fileLocation=os.path.join(filePath, fileName)
fileLocation=(filePath+ fileName)

colonCount = 0
tFileLoc = ''
for char in fileLocation:
    if char ==':':
        colonCount+=1
        if colonCount==1:
            tFileLoc+=':'
        elif colonCount==2:
            tFileLoc+=('hrs')
        elif colonCount==3:
            tFileLoc+=('mins')
    else:
        tFileLoc+=(char)
fileLocation=tFileLoc


print('GEG',fileLocation)#filePath,'\n',fileName,'\n',
#fileLocation , str('audioNameStream_'+ startTime+ '.txt'
#fileLocation = 'C:/Users/matth/codeProjects/speechNameTracker/transcripts/'
# list of names
nameList = ['matthew', 'adam', 'lauren', 'jared', 'jason','couldnotunderstandwords']


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
print(datetime.now())
def gotName(sentence, calledDict):
    
    wordList = re.sub("[^\w]", " ",  sentence).split()
    for word in wordList:
        if word.lower() in calledDict:
            calledDict[word.lower()]+=1


# getAudio() was yoinked from internet https://www.geeksforgeeks.org/personal-voice-assistant-in-python/
def get_audio():

    rObject = sr.Recognizer()
    audio = ''
  
    with sr.Microphone() as source:
        #print("Started...") # testing
          
        # recording the audio using speech recognition
        audio = rObject.listen(source, phrase_time_limit = 5) # limit 5 secs ## LOOK INTO SNOWBOY hotword detector (hover over "listen" it gives info) # more info here: https://www.geeksforgeeks.org/hotword-detection-with-python/
    #print("Stop.") # testing
  
    try:
  
        text = rObject.recognize_google(audio, language ='en-US')
        #print("You : ", text) # testing
        return text
  

    except:
  
        #print("Could not understand your audio, PLease try again !") # testing
        return 'couldnotunderstandwords'


#students = nameList
#timesCalled = [googleCalledDict[nameList[0]],googleCalledDict[nameList[1]],googleCalledDict[nameList[2]],googleCalledDict[nameList[3]],googleCalledDict[nameList[4]]]

keys = googleCalledDict.keys()
values = googleCalledDict.values()
#plt.ion()
#figure=plt.bar(keys,values)
'''fig = plt.figure()
bars = plt.bar(keys, values)

def animate(i):
    keys = googleCalledDict.keys()
    values = googleCalledDict.values()'''   

#ani = FuncAnimation(plt.bar(keys,values),animate, interval=10)
plt.ion()
fig = plt.figure()
ax=fig.add_subplot(1,1,1)
x=googleCalledDict.keys()
y=googleCalledDict.values()
ax.bar(x,y)
fig.autofmt_xdate()
plt.draw
while True:
    googleTemp = get_audio()
    try:
        gotName(googleTemp, googleCalledDict)
    # allows the program to exit when ctrl+c
    except KeyboardInterrupt:
        exit('You interrupted through the keyboard.')
    # sometimes theres an error, maybe if it can't understand what it hears
    except:
        print('There was a problem.')
    print(datetime.now())
    print(googleTemp)
    print(googleCalledDict)
    #print(str('audioNameStream_'+ startTime+ '.txt'))
    print(fileLocation)
    f = open(fileLocation, 'a') #, str('audioNameStream_'+ startTime+ '.txt'),
    f.write(str(datetime.now())+'\n'+ str(googleTemp)+ '\n'+ str(googleCalledDict)+ '\n\n')
    f.close()

    # sets up keys and values for bar chart
    #keys = googleCalledDict.keys()
    #values = googleCalledDict.values()
    y=googleCalledDict.values()
    ax.clear()
    ax.bar(x,y)
    plt.draw()
    ##ani = FuncAnimation(plt.bar(keys,values),animate, interval=10)
    
    ##plt.show()

    '''#plt.bar(keys,values) # makes bar chart
    figure.canvas.draw()
    figure.canvas.flush_events()
    plt.show(block=False) # shows bar chart'''






###old stuff
'''
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

'''