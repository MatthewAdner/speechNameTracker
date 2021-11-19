#import sounddevice as sd
 
import speech_recognition as sr
import re
import matplotlib.pyplot as plt

print('iran')
mLis = sr.Microphone.list_microphone_names()

mic = sr.Microphone(device_index=1)#mLis.index('Microphone (Logitech Mic (Commu'))
print(sr.Microphone.list_microphone_names())

# list of names
nameList = ['matthew','adam','lauren','jared']

googleCalledDict = {}
sphinxCalledDict = {}
for name in nameList:
    googleCalledDict[name]=0
    sphinxCalledDict[name]=0

# function to check for a word
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

            googleTemp = r.recognize_google(audio)
            print('google:')
            gotName(googleTemp, googleCalledDict)
            print(googleTemp)
            print(googleCalledDict)

        except KeyboardInterrupt:
            exit('You interrupted through the keyboard.')
        except:
            print('There was a problem.')

