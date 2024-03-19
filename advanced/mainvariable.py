# __name__ is a variable set by python interpreter at runtime. If this program is
# the first module being run, __name__ will be "__main__"

print(__name__)

# can check if module is being run directly, or called by another program
if __name__ == "__main__":
    print("Running module directly")