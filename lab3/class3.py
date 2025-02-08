#Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.

class Shape:
    def __init__(self):
        self.area = 0
    def findArea(self):
        return self.area
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def findArea(self):
        self.area = self.length * self.width
        return self.area

# Let's test an area method
a = int(input("Enter length: "))
b = int(input("Enter width: "))
reck = Rectangle(a, b)
print("Default Area:", reck.area)
reck.findArea()
print("Calculated Area:", reck.area)