'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

str = input("Write a string: ")
str = str.split(" ")

nlist = []
for word in str:
    l = list(word)
    l = tuple(l)
    nlist.append(l)
print(nlist)