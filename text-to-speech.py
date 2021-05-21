# Import the required module for text
# to speech conversion
from gtts import gTTS
import pyttsx3
import os
import speech_recognition as sr
# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
with open('text.txt') as f:
    mytext = f.read()

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("youraudio.mp3")

# Playing the converted file
music_dr= 'D:\\Python\\texttospeech\\'
songs= os.listdir(music_dr)
os.startfile(os.path.join(music_dr,songs[0]))
