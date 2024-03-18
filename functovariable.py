# creating a variable
def hello():
    print("hello")

# ponting variable "message" to memory address of function "hello"
message = hello

# can now call message() in the same way as hello()
message()