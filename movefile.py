# moving a file or folder with os.replace
import os

source = "files/file.txt"
destination = "C:\\Users\\Louis\\Desktop\\test.txt"

try:
    if os.path.exists(destination):
        print("File already present")
        os.replace(source, destination) # replace moves the file
except FileNotFoundError:
    print(source+" was not found")

