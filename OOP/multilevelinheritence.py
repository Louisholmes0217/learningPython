# multi-level iheritence is a child class created from another child class

class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("This animal is eating")    

class Dog(Animal):
    def bark(self):
        print("This dog is barking")

dog = Dog()

print(dog.alive) # from organism class
dog.eat()        # from animal class
dog.bark()       # from dog class