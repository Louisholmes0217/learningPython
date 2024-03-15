# deleting file or folder
import os
import shutil

with open("deleteme.txt", "w"):
    pass
try:    # remove file
    os.remove("deleteme.txt") 
except FileNotFoundError:
    print("file was not found")

try:    # remove empty folder
    os.rmdir("testfolder")
except FileNotFoundError:
    print("folder not found")

try:
    shutil.rmtree("path")
except FileNotFoundError:
    print("folder not found")
