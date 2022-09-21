from os import system

def speak(text , wantOutput="_true"):
    f = open("cache.txt","w")
    f.write(f"{text}")
    f.close()
    if wantOutput == "_true":
        print(f"{text}")
    else:
        pass
    system(f"festival --tts ./cache.txt")


if __name__ == '__main__':
    print("Fuck you")