# abstract classes prevent a user from creating an object of that class
# abstract method must be overrided when, as it is merely an empty template
from abc import ABC, abstractmethod  # ABC stands for abstract class


# to turn a class into an abstract class, initialize it from the parent ABC class
class Vehicle(ABC): # inheriting from ABC

    @abstractmethod # this is a decorator to make this method abstract
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")
    
    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):
    
    def go(self):
        print("You drive the motorcycle")
    
    def stop(self):
        print("This motorcycle is stopped")

# vehicle = Vehicle() # fails
car = Car()
motorcycle = Motorcycle()
car.go()
motorcycle.go()