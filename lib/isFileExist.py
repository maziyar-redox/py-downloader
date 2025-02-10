import os

def isFileExist(fileName):
    isfile = os.path.isfile(fileName)
    if isfile == True:
        return True
    else:
        return False