import speech_recognition as sr
from speechDic import speak
def listen():
    microphone = sr.Recognizer()	
    with sr.Microphone() as live_phone:
        microphone.adjust_for_ambient_noise(live_phone)
        audio = microphone.listen(live_phone)
        try:
            phrase = microphone.recognize_google(audio, language='en')
            return phrase
        except sr.UnkownValueError:
            speak("Could you please repeat that again!")
if __name__ == '__main__':
    microphone = sr.Recognizer()	
    with sr.Microphone() as live_phone:
        microphone.adjust_for_ambient_noise(live_phone)
        audio = microphone.listen(live_phone)
        try:
            phrase = microphone.recognize_google(audio, language='en')
            print(f"You just said {phrase}")
        except sr.UnkownValueError:
            print(sr)
            speak("Could you please repeat that again!")