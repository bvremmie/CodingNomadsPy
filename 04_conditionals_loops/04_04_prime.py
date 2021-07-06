'''
Print out every prime number between 1 and 100.

'''

for n in range(1, 101): #number in range of 0-100
    for i in range(2, n-1):
        if n // i != 0:
            print(n)
        # else:
        #     n // i == 0:
