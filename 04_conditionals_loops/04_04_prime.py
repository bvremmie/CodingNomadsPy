'''
Print out every prime number between 1 and 100.

'''


for n in range(1, 101): #number in range of 0-100
    if n % 1 == 0 and n % n == 0: #if n/2 is not 0 (so odd number)
        print(n)