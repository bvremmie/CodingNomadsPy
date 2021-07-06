'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
from itertools import count

str = (input("Give me a string: ")).lower()
str = str.split()


occ = {}
occ = dict.fromkeys(str, 0)
# dict[str] = str.count(str)

for word in occ:
    c = str.count(word)
    occ[word] = c
    m = max(occ, key=occ.get)
print(m)



# cnt = str.count(word)
#    # dict[word] = cnt

# max = 0
# for word in occ:

#     if cnt > max:
#         max = cnt
#         dict[str] = max
#     if max(occ, key=occ.get):
#         print(occ)
#
#
# strList = []