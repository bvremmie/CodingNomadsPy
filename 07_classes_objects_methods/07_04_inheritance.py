'''
CLASSES AND INHERITANCE
=======================

1) Define an empty Movie class.

2) Add a dunder init method that takes two arguments "year" and "title"

3) Create a sub-class called "RomCom" that inherits from the Movie class

4) Create another sub-class of the Movie class called "ActionMovie"
    that overwrites the dunder init method of Movie and adds another
    instance variable called "pg" that is set by default to the number 13.

5) EXTRA: If you finish early, use the time to practice flushing out these
    classes and white-boarding code. What attributes could a Movie class
    contain? What methods? What tricks can you use through inheritance?
    Any class attributes you could add?

'''

class Movie:
    def __init__(self, year, title):
        self.year = year
        self.title = title

    def __str__(self):
        return f"Year: {self.year}\nTitle: {self.title}"

class RomCom(Movie):
    pass

class ActionMovie(Movie):
    def __init__(self, year, title, pg=13):
        super().__init__(year, title)
        self.pg = pg


ori = Movie(2020, "A Year to Remember")
print(ori)
rom = RomCom(2000, "The Notebook")
print(rom)
action = ActionMovie(2000, "Fast and Furious")
print(action)
print(f"PG: {action.pg}")