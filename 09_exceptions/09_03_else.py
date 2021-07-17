'''
Write a script that demonstrates a try/except/else.

'''
# while True:

try:
    guess = int(input("Try to guess a number that I'm thinking of: "))
except ValueError:
    print("Again, try to guess a number: ")
else:
    print("Sorry, that's not the number I'm thinking of. Better luck next time :)")