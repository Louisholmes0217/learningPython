# writing a file
with open("files/writtenfile.txt", "w") as file:    # "w" opens file in write mode
    file.write("This has been written to the file from python\n")


# appending to a file
with open("files/writtenfile.txt", "a") as file:
    file.write("This is a new line")