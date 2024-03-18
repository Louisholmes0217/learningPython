# passing an object as an argument to a function

class Car:  # class containing a variable
    colour = None

class Motorcycle:  # class containing a variable
    colour = None

def change_colour(vehicle, colour): # function takes objects as a variable
    vehicle.colour = colour

car_1 = Car()
car_2 = Car()
car_3 = Car()
bike_1 = Motorcycle()

print(car_1.colour, car_2.colour, car_3.colour)

change_colour(car_1, "red")
change_colour(car_2, "green")
change_colour(car_3, "blue")
change_colour(bike_1, "black")

print(car_1.colour, car_2.colour, car_3.colour)
print(bike_1.colour)