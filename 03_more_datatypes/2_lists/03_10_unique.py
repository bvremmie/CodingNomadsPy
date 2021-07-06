'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''

from itertools import count
list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]

newlist = []
for ch in list_:
    num = list_.count(ch)
    if num == 1:
        newlist.append(ch)
print(newlist)