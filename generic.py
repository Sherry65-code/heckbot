from os import system, name
from sys import exit 

def checkSYS():
    if name == "nt":
        return "Windows"
    else:
        return "Linux"

def fuckoff():
    if checkSYS() == "Windows":
        print("As you are using Windows, Speech Dictation wont work on this program")
        exit()
    else:
        pass

def passtosystem(_command):
    system(f"{_command}")

def welcomeUser():
    print("Hello, I am heck bot. How may i help you.")
    return "Hello, I am heck bot. How may i help you."

def engage():
    input()

if __name__ == '__main__':
    print("Fuck you")