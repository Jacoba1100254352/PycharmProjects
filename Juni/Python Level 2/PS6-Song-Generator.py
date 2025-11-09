"""
Use pysynth to build a song generator that asks the user to enter in notes to add to the song!
"""

import pysynth


# Reminder for using psynth:
# 1) You can see the project files by clicking the file icon on the sidebar to the left!
# 2) Do not click on the wav file until the program is finished running (i.e. once you see the blue Run button again instead of the red Stop button)

song = []

while True:
	note = input("Enter a note to add to your song! Or enter 1 to stop.")
	
	if note == "1":
		break
	
	song.append((note, 4))

pysynth.make_wav(song, fn='song.wav')

# advanced version:
'''
song = []

while True:
  note = input("Enter a note to add to your song! Or enter 1 stop.")

  if note == "1":
    break

  duration = input("Enter the duration for the previous note: 1, 2, 4, or 8.")

  song.append((note, int(duration)))

pysynth.make_wav(song, fn='song.wav')
'''

# Additional Functionality
"""
acceptableNotes = ["stop", "a0", "a#0", "b0", "c8"]
for letter in "abcdefg":
  for i in range(1,8):
    acceptableNotes.append(letter+str(i))
    if letter not in "eb":
      acceptableNotes.append(letter+"#"+str(i))
for letter in "abcdefg":
  acceptableNotes.append(letter)
  if letter not in "eb":
    acceptableNotes.append(letter+"#")
print(acceptableNotes)

acceptableDuration = [1,2,4,8]

mySong = []
while True:
  note = input("Enter a note! or enter stop to stop: ").lower()
  while note not in acceptableNotes:
    note = input("Please enter a correct note! or enter stop to stop: ").lower()

  if note == "stop":
    break
    
  duration = int(input("Enter a duration: "))
  while duration not in acceptableDuration:
	duration = int(input("Please enter a correct duration: "))
  
  mySong.append((note,duration))



pysynth.make_wav(mySong, fn='name.wav')

"""
