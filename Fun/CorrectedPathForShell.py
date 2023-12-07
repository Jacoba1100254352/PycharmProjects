import sys


def needsBackSlash(char):
    needsBackSlashList = [' ', '(', ')', '\'']
    return char in needsBackSlashList


def correctDownloadFilePath(downloadFilePath):
    insertLocations = []

    # Fix the ends of the file path
    while downloadFilePath[0] == ' ':
        downloadFilePath = downloadFilePath[1:]
    if downloadFilePath[0] != '/':
        downloadFilePath = '/' + downloadFilePath
    if downloadFilePath[len(downloadFilePath) - 1] != '/':
        downloadFilePath += '/'

    # Find the positions that need a '/'
    for index in range(len(downloadFilePath)):
        if needsBackSlash(downloadFilePath[index]) and downloadFilePath[index - 1] != '\\':
            insertLocations.append(index + len(insertLocations))  # with each insert the new location shifts by +1
    # Add the '/' to the correct locations
    for index in insertLocations:
        downloadFilePath = downloadFilePath[:index] + '\\' + downloadFilePath[index:]
    return downloadFilePath


print(correctDownloadFilePath(sys.argv[1]))
