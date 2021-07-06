'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''
from itertools import count

string = (input("Give me a sentence: "))
string = string.lower()

#string = "give me a sentence"

dict = {}
for i in string:
    cnt = string.count(i)
    dict[i] = cnt
print(dict)

