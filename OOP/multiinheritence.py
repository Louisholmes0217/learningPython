# multi inheritence is where a child class is created from several parent
# classes

class Prey:
    def flee(self):
        print("This animal flees")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Predator, Prey):
    pass

fish = Fish()
hawk = Hawk()
rabbit = Rabbit()

fish.flee()
fish.hunt()

hawk.hunt()
rabbit.flee()