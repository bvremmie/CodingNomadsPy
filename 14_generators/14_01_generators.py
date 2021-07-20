'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''

gen = (i for i in range(5))
print(gen)

for x in gen:
    print(x+1)