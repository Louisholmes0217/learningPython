# typing is a concept where the class of an object is not as important
# than the methods and attributes of the class. 

class Duck:
    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("This duck is quacking")

class Chicken:
    def walk(self):
        print("This chicken is walking")
    def talk(self):
        print("This chicken is clucking")

class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken) # This can be duck or chicken, it doesnt care about the specific of the object.
                      # As long as the method is present and correct, it will run. So long as duck and
                      # chicken both have a .walk and .talk, the code function will run.