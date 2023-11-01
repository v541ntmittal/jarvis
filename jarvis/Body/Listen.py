#whether we speak in hindi or english it will understand both by translating it in english
import speech_recognition as sr
from googletrans import Translator

#first it will listen whether we speak in hindi or english
def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)

    try:
        print("Recognising....")
        query= r.recognize_google(audio,language="hi")

    except:
        return ""
    
    query = str(query).lower()
    return query


#Translating it to English 
def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You : {data}.")
    return data

# Connecting both functions
def MicExecusion():
   query = Listen()
   data = TranslationHinToEng(query)
   return data

