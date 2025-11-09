"""
Use pysynth to program a song of your choice, programming the notes and their duration into a list!
"""

import pysynth


# Reminder for using psynth:
# 1) You can see the project files by clicking the file icon on the sidebar to the left!
# 2) Do not click on the wav file until the program is finished running (i.e. once you see the blue Run button again instead of the red Stop button)

# example:
potter = [('b3', 4), ('e', -4), ('e4', -4), ('g', 8), ('f#', 4), ('e', 2), ('b', 4), ('a', -2), ('f#', 2)]
pysynth.make_wav(potter, fn='potter.wav')

# write the code to build your own song below:
