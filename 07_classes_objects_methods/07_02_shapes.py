'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f"This rectangle has a length of {self.length} ft and a width of {self.width} ft."

    def area(self):
        area = self.length * self.width
        return f"The area of this rectangle is {area} ft."

    def per(self):
        per = 2*self.length + 2*self.width
        return f"The perimeter of this rectangle is {per} ft."


rectangle = Rectangle(8,6)
print(rectangle)
print(rectangle.area())
print(rectangle.per())

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"The radius of this circle is {self.radius} ft."

    def area(self):
        area = 2*3.14*self.radius**2
        return f"The area of this circle is {area} ft."

    def circ(self):
        circ = 2*self.radius*3.14
        return f"The circumference of this circle is {circ} ft."


circle = Circle(3)
print(circle)
print(circle.area())
print(circle.circ())