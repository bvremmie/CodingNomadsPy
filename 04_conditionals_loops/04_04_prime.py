'''
Print out every prime number between 1 and 100.

'''

for n in range(1, 100): #number in range of 0-100
    #print(n)
    is_prime = True
    for i in range(2, n):
            if n % i == 0:
                #not prime
                is_prime = False
                break
    if is_prime:
        print (n)