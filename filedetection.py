# os library to work with windows
import os

path = "files/file.txt"     # setting file path

if os.path.exists(path):    # returns bool if file location is valid
    print("valid file location")

else:
    print("invalid file location")

if os.path.isfile(path):    # returns true if file is an actual file
    print("the file is an actual file")
else:
    print("the file is not an actual file")

path = "files"
if os.path.isdir(path): # checking if path leads to directory
    print("this is a directory")
else:
    print("this is not a directory")