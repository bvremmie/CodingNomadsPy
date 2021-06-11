# class Ingredient:
#   """Models an Ingredient. Currently only carrots!"""
#   def __init__(self, name, amount): # this is defining the method within the class
#     self.name = 'carrot' # first attribute of the class Ingredient
#     self.amount = 3      # second attribute of the class Ingredient
#
#
# i = Ingredient("carrot", 4)
# print(i.name, i.amount)
#
#
# class Point:
#     """Represents a point in 2-D space."""
#
#     def __init__(self, x=0, y): #x=0 v x, there is no difference
#         self.x = x
#         self.y = y
#
#
# p = Point(5, 10)
# print(sum(p.x, p.y))
#

class Car:
    """defining CAR CLass"""
    def __init__(self, model, year, speed=0):
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        """"add 5 to speed"""
        self.speed += 5

    def brake(self):
        """ sub 5 from speed if its not 0 """
        if self.speed == 0:
            self.speed = 0
        else:
            self.speed -= 5

    def honk_horn(self):
        """print statement"""
        return f"{self.model} goes 'beep beep'"

my_car = Car("Toyota", 1975)
print(my_car.speed)