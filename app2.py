import googletrans
import speech_recognition
import gtts
import playsound

recognizer =speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("say something")
    voice =recognizer.listen(source,None,3)
    text =recognizer.recognize_google(voice,language="hi")
    print(text)


translator = googletrans.Translator()
translation = translator.translate(text,dest="en")
print (translation.text)
converted_audio =gtts.gTTS(translation.text,lang="en")
converted_audio.save("hello1.mp3")
playsound.playsound("hello1.mp3")
#print(googletrans.LANGUAGES)
