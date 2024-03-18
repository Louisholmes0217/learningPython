# A class is a logical way of grouping associated functions,(methods)
# and state.
# An object is an instance of a class.

class Car():
    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.colour = colour
        self.year = year

    def drive(self):
        print("This {} is driving!".format(self.model))
    
    def stop(self):
        print("This {} is stopped!".format(self.model))

car_1 = Car("chevy", "corvette", "2021", "blue")
car_2 = Car("Ford", "Mustang", "2022", "red")

print(car_1.make)
car_1.drive()
car_1.stop()
car_2.drive()
car_2.stop()

