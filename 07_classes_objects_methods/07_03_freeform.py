'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets at least three attributes
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Create at least two instances of each class.
- Once the objects are created, change some of their attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, card games, sports teams, trees, people etc...

'''

class Bottle:
    def __init__(self, shape, max_amt, color):
        self.shape = shape
        self.max_amt = max_amt
        self.color = color

    def __str__(self):
        return f"This {self.color} bottle is {self.shape}-shaped and can hold {self.max_amt} oz."

galBottle = Bottle("gallon", 180, "teal")
print(galBottle)

brita = Bottle("tumbler", 32, "orange")
print(brita)

class Elephant:
    def __init__(self, age, weight, color):
        self.age = age
        self.weight = weight
        self.color = color

    def __add__(self, other):
        return f"Combo elephant: {self.age + other.age} years old and {self.weight + other.weight} lbs."

    def __str__(self):
        return f"This {self.color} elephant is {self.age} years old and weighs {self.weight} lbs."

a = Elephant(5, 312, "brown")
b = Elephant(2, 100, "gray")
c = a + b
print(a)
print(b)
print(c)