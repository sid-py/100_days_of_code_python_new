import gtts
from playsound import playsound


# make request to google to get synthesis
tts = gtts.gTTS("The specified device is not open or is not recognized by MCI.")

tts.save("hello.mp3")

playsound("hello.mp3")