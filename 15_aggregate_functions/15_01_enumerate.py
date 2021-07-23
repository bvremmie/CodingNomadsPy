'''
Demonstrate the use of the .enumerate() function.
'''

my_list = ["apple", "banana", "orange"]

obj1 = []
for index,fruit in enumerate(my_list):
    yer = (index, fruit)
    l = list(yer)
    l = tuple(l)
    obj1.append(l)


print(obj1)