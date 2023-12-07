import pysynth

# Reminder for using psynth:
# 1) You can see the project files by clicking the file icon on the sidebar to the left!
# 2) Do not click on the wav file until the program is finished running (i.e. once you see the blue Run button again instead of the red Stop button)
acceptableNotes = ["stop", "a0", "a#0", "b0", "c8"]
# acceptableNotes += [f"{l}{sharp}{i}" for l in "abcdefg" for sharp in (["", "#"] if l not in "eb" else [""]) for i in range(9)]
for letter in "abcdefg":
    # Add normal/default note names without octave number
    acceptableNotes.append(letter)
    # Add note names with sharp without octave number
    if letter not in "eb":
        acceptableNotes.append(letter + "#")

    # Add note names with octave number
    for i in range(1, 8):
        acceptableNotes.append(letter + str(i))
        # Add note names with sharp with octave number
        if letter not in "eb":
            acceptableNotes.append(letter + "#" + str(i))

# print(acceptableNotes)

mySong = []
notes = {"whole": 1, "half": 2, "quarter": 4, "eighth": 8, "sixteenth": 16}
while True:
    Note = input("Enter a note to add to your song! Or add 1 to stop: ")
    if Note == "1":
        break

    while Note not in acceptableNotes:
        Note = input("Please enter a correct note! or enter stop to stop: ").lower()
    Duration = input("Enter a the duration for the previous note. Whole, half, quarter, eighth, or sixteenth: ").lower()
    mySong.append((Note, notes[Duration]))
    pysynth.make_wav(mySong, fn='name.wav')
