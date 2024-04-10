import pysynth


# Reminder for using psynth:
# 1) You can see the project files by clicking the file icon on the sidebar to the left!
# 2) Do not click on the wav file until the program is finished running (i.e. once you see the blue Run button again instead of the red Stop button)

song = []
notesDict = {"whole": 1, "half": 2, "quarter": 4, "eighth": 8}

while True:
	note = input("Enter a note to add to your song! Or enter 1 stop. ")
	
	if note == "1":
		break
	
	duration = input("Enter the duration for the previous note: whole, half, quarter, or eighth. ")
	
	song.append((note, notesDict[duration]))

pysynth.make_wav(song, fn='song.wav')
