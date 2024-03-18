# classes can inherit the methods and variables of another class
# the parent class is the top level class, and the classes derived
# from the parent class are the child classes

class Animal:
    alive = True
    
    def __init__(self):
        pass
    def eat(self) :
        print("This animal is eating")
    
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):   # child class for Rabbit
    def run(self):
        print("This rabbit is running")
    
class Fish(Animal):     # child class for Fish
    def swim(self):
        print("This fish is swimming")
    
class Hawk(Animal):     # child class for Hawk
    def fly(self):
        print("This hawk is flying")

# creating objects from the child classes
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# calling methods from objects
hawk.sleep()
print(fish.alive)
rabbit.eat

# calling child specific methods
hawk.fly()
fish.swim()
rabbit.run()