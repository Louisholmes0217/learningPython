# you can override a method within a parent class
# in python to allow for a more specific implementation
# according to the needs of that class

class Animal:   # parent class
    def eat(self):
        print("This animal is eating!")

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot!")

animal = Animal()
animal.eat()
rabbit = Rabbit()
rabbit.eat()
