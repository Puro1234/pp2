#Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape:
    def __init__(self):
        self.area = 0
    def findArea(self):
        return self.area
    
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def findArea(self):
        self.area = self.length * self.length
        return self.area


# Let's test an area method
a = int(input("Enter length of a square: "))
sqr = Square(a)
print("Default Area:", sqr.area)
sqr.findArea()
print("Default Area:", sqr.area)