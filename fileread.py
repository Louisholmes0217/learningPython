# reading files

with open("files/file.txt") as FILE:    # runs indented code and closes automatically after
    print(FILE.read())

print(FILE.closed)


try:                                    # safely working with and opening file with exceptions
    with open("files/file.txt") as FILE:
        print(FILE.read())
except FileNotFoundError:
    print("file not found")

print("Done")