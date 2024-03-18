# method chaining is calling multiple class methods sequentially
# each method performs an action on the same object and returns self
 
class Car:
    def turn_on(self):
        print("You start the engine")
        return self         # returning self to allow sequential execution
    def brake(self):
        print("You step on the brakes")
        return self
    def drive(self):
        print("You drive the car")
        return self
    def turn_off(self):
        print("You turn off the engine")
        return self

car = Car()

#car.turn_on()
#car.drive() This code can be represented as

#car.turn_on().drive() # this runs the first method, and then runst the second against the
                      # returned value, being "self" which is car.

#car.turn_on().drive().brake().turn_off()
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()