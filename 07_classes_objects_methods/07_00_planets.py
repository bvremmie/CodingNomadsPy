'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet:
    def __init__(self, name, order, weight):
        self.name = name
        self.order = order
        self.weight = weight

    def __str__(self):
        return f"The planet {self.name} is the {self.order}th planet from the sun and weighs {self.weight} lbs."
    pass

jupiter = Planet("Jupiter", "7", 3212.78)

print(jupiter)