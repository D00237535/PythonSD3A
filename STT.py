import speech_recognition

recongnizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say something!")
    audio = recongnizer.listen(source)
    print("Google Speech Recognition thinks you said:")
    print(recongnizer.recognize_google(audio))



