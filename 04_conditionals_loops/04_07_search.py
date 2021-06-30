'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

i = int(input("Give me a number between 0 and 1,000,000,000: "))

n = 0
while n < 1000000000:
    if n != i:
        n += 1
    else:
        print(n)
        break