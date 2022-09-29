import speech_recognition as sr   # for speech-to-text
from gtts import gTTS   # for text-to-speech
import transformers     # for language model
import os
import time
import datetime
import numpy as np

# building the AI
class ChatBot():
    def __init__(self, name):
        print("--- starting up ", name, " ---")
        self.name = name

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("listening...")
            audio = recognizer.listen(mic)
            self.text = "ERROR"
        try:
            self.text = recognizer.recognize_google(audio)
            print("Me: ", self.text)
        except:
            print("Me: ERROR")

    @staticmethod
    def text_to_speech(text):
        print("Siri: ", text)
        try:
            speaker = gTTS(text=text, lang="en", slow=False, )
            speaker.save("res.mp3")
            statbuf = os.stat("res.mp3")
            mbytes = statbuf.st_size / 1024
            duration = mbytes / 200
            os.system("start res.mp3")  # windows start
            # os.system("close res.mp3")
            time.sleep(int(50 * duration))
            os.remove("res.mp3")
        except AssertionError as e:
            print("Siri: ERROR")

    def wake_up(self, text):
        return True if self.name in text.lower() else False

    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime('%H:%M')


# Running the AI
if __name__ == "__main__":
    ai = ChatBot(name="Siri")
    nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
    os.environ["TOKENIZERS_PARALLELISM"] = "true"
    ex = True
    while ex:
        ai.speech_to_text()
        # wake up
        if ai.wake_up(ai.text) is True:
            res = "Hello I am Siri, What can I do for you?"
        # action
        elif "time" in ai.text:
            res = ai.action_time()
        # respond politely
        elif any(i in ai.text for i in ["thank", "thanks"]):
            res = np.random.choice(["you're welcome", "anytime!", "no problem", "alright grand"])
        elif any(i in ai.text for i in ["exit", "close"]):
            res = np.random.choice(["bye", "goodbye", "see ya", "see you soon"])
            ex = False
        # conversation
        else:
            if ai.text == "ERROR":
                res = "Sorry, come again"
            else:
                chat = nlp(transformers.Conversation(ai.text), pad_token_id=50256)
                res = str(chat)
                res = res[res.find("bot: ") + 6:].strip()
        ai.text_to_speech(res)