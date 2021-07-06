'''

Write a script that removes all duplicates from a list.

'''

list_ = [1, 2, 3, 4, 3, 4, 5]

newlist = []
for i in list_:
    c = list_.count(i)
    if c == 1:
        newlist.append(i)
print(newlist)