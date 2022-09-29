import pyttsx3

engine = pyttsx3.init()

"""VOLUME"""
voices = engine.getProperty('voices')

volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume', 1.0)    # setting up volume level  between 0 and 1

for voice in voices:
    engine.setProperty('voice', voice.id)  #changing index, changes
    engine.say("I can talk")
    engine.runAndWait()
    engine.stop()