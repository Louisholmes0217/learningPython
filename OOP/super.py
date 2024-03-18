# super() funtion is used to give access to the methods of a parent class.
# returns a temporary instance of a parent class when called.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width 

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width) # calling the innit of Rectangle that will initialize self.width and self.length

    def area(self):
        return self.length*self.width
    
class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width) # calling the innit of Rectangle that will initialize self.width and self.length
        self.height = height
        
    def area(self):
        return self.length*self.width*self.height

square = Square(5, 5)
cube = Cube(5, 5, 5)

print(square.area())