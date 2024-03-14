# conditional if statement
age = input("Enter your name\n:    ")
age = int(age)

if age >= 18:
    print("You are an adult")
elif age <= 18:
    print("You are a minor")
else:
    print("Invalid age")

