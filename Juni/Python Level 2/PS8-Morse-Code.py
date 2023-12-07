import pysynth

# Reminder for using psynth: 
# 1) You can see the project files by clicking the file icon on the sidebar to the left!
# 2) Do not click on the wav file until the program is finished running (i.e. once you see the blue Run button again instead of the red Stop button)

morseDict = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
             "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-",
             "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
             "z": "--.."}


# 1. Define a function that takes in a message and converts that message into morse code. (Make sure to put extra spaces inbetween your words.) Using the function, ask the user for a message and print out the translated message.

def translateToMorseCode(msg):
    morseMsg = ""
    for letter in msg:
        if letter == " ":
            morseMsg += "  "
        else:
            morseMsg += morseDict[letter] + " "
    return morseMsg


msg = input("Type in a message to translate into morse code (in all lowercase): ")
print(translateToMorseCode(msg))


# 2. Define a function that takes in a message and converts that message into musical morse code. Each dot should be a C for an eighth note, and each dash should be a C for a half note. Rest for a half note inbetween each word and an eighth note between each dot or dash.

def translateToMorseCodeMusic(msg):
    song = []
    for letter in msg:
        if letter == " ":
            song.append(('r', 2))
        else:
            morseChar = morseDict[letter]
            for char in morseChar:
                if char == ".":
                    song.append(('c', 8))
                elif char == "-":
                    song.append(('c', 2))
                song.append(('r', 8))

    return song


msg = input("Type in a message to translate into morse code music (in all lowercase): ")
pysynth.make_wav(translateToMorseCodeMusic(msg), fn="morseSong.wav")
