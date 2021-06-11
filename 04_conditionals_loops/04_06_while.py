'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''

#range from 1-1000
num = range(1,1000+1)

for n in num:
    print(n)
    i=0
    if i % 5 == 0:

    n += 5