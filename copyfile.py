# copyfile() copies file contents
# copy() copies file and permission mode, can also copy directories
# copy2() copies all metadata with previous step

import shutil # library for copying files
shutil.copyfile("files/file.txt", "files/copied.txt") # copies file

