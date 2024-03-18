class Car():

    # class variables are assigned for the class and every instance of the class
    wheels = 4

    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.colour = colour
        self.year = year

car_1 = Car("chevy", "corvette", "2021", "blue")
car_2 = Car("Ford", "Mustang", "2022", "red")

print(car_1.wheels)
print(car_2.wheels)

print(Car.wheels)    # accessing wheels of the class
car_1.wheels = 2    # changing just car_1 wheels
print(car_1.wheels)

Car.wheels = 2    # changing all instances by modifying the class variable
print(car_2.wheels)
