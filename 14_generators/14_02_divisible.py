'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''

gen = (i for i in range(5556))

for x in gen:
    if x % 1111 == 0 and x != 0:
        print(x)