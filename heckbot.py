from speechDic import speak
from generic import fuckoff, welcomeUser, passtosystem
from speechSynth import listen
fuckoff()
speak(welcomeUser(), "_f")

while True:
    try:
        print(">", end=" ")
        query = listen()
        print(query)
        if ("hi" in query or "hai" in query or "hello" in query):
            speak("Hi, How are you ?")
        elif ("how are you" in query):
            speak("I am fine, how about you ?")
        elif ("i" in query and "am" in query and "fine" in query):
            if ("not" in query):
                speak("Oh, i am sorry for that.")
            else:
                speak("Thats good to you.")
        elif ("bye" in query):
            speak("bye")
            break
        elif ("open" in query):
            if ("chrome" in query):
                passtosystem("google-chrome-stable &")
            elif ("zoom" in query):
                passtosystem("zoom &")
            elif ("youtube" in query):
                passtosystem("google-chrome-stable https://youtube.com/ &")
            elif ("music"):
                passtosystem("google-chrome-stable https://sherry65-code.github.io/muzik.com")
        else:
            speak("Sorry, I cannot help you with that.")
    except Exception as e:
        speak("An Error Occured. We will try to fix this problem as soon as possible")
        break
    except KeyboardInterrupt:
        speak("Bye! Have a nice day")
        break