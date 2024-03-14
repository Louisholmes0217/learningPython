# **kwargs will pack all arguments into a dictionary
# useful for adding "flags" to program or function

def hello(**kwargs):
    print("Hello " + kwargs["first"] + " " + kwargs["last"])

hello(first="Awesome", last="Name")


def hello2(**names):
    print("Hello", end=" ")
    for key,value in names.items():
        print(value, end=" ")

hello2(title = "Mr", first = "Awesome", middle="Bestest", last="Name")