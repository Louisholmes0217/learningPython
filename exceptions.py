# exception is an event detected during runtime that interrupts the program

try:    # try block
    numerator = int(input("Please enter a number to divide: "))
    denominator = int(input("Please enter a number to divide by: "))
    result = numerator/denominator
except ZeroDivisionError as e:   # catching zero / errors
    print(e)
    print("You can't divide by zero!")

except  ValueError as e:        # catching value errors
    print(e)
    print("Enter only numbers please")

except Exception as e:          # catching any unknown errors
    print(e)
    print("Unknown Error")

else:
    print(result)               # running if no error is detected

finally:
    print("This will always execute")       # always runs regardless of errors