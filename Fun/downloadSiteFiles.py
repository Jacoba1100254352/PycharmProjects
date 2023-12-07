import os.path
import time

import wget
from requests_html import HTMLSession

'''   Functions   '''


def correctDownloadFilePath(path):
    # Fix the ends of the file path
    while path[0] == ' ':
        path = path[1:]
    if path[0] != '/':
        path = '/' + path
    if path[len(path) - 1] != '/':
        path += '/'
    return path


'''   Main Code   '''
session = HTMLSession()

downloadFilePath = "C:\Users\jacobda2\Documents"
url = "http://math.byu.edu/~vianey/Math334/Classes/"
fileType = ".pdf"
toPrint = []

# get all artists on the main page except the parent directory link
downloadFilePath = correctDownloadFilePath(downloadFilePath)
artists = session.get(url).html.xpath("//td[not(contains(a, 'Parent Directory'))]/a")
artists = [url + a.attrs["href"] for a in artists]

# Used to update the user as to the current progress of the program, though not entirely necessary
timeWaiting = time.time()

# start sorting and digging until only the specified fileType are kept
print("Sorting...")
while len(artists) != 0:

    artistsCopy = artists
    for artist in artistsCopy:

        # if not the file to download continue down the tree
        if fileType not in os.path.basename(artist):

            # make sure only valid links are being processed, and they're not the file we are looking for
            if artist[len(artist) - 1] != '/':
                artists.remove(artist)
                continue

            # get full working path and all sub-links besides the parent directory available
            sublinks = session.get(artist).html.xpath("//td[not(contains(a, 'Parent Directory'))]/a")

            # add the remaining head links to the artists to sort and remove the current artist (replaced by its lower links [now visited])
            artists.remove(artist)
            artists += [artist + link.attrs["href"] for link in sublinks]

        # This is the file we want, add it to the to print list
        else:
            toPrint.append(artist)
            artists.remove(artist)

        # Used to update the user as to the current progress of the program, though not entirely necessary
        if time.time() - timeWaiting > 60:
            print("Still sorting...")
            timeWaiting = time.time()

# Download all of the collected links/files
print(toPrint)
print("Downloading...")
for file in toPrint:
    try:
        wget.download(file, f'{downloadFilePath + os.path.basename(file)}')
    except:
        print("A problem occurred with file: " + str(file))
print("Finished!")
