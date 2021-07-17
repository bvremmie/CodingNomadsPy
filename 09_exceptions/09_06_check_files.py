'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

file_name = 'integers.txt'


try:
    with open(file_name, "r") as fin:
        file = fin.readlines(1)
except OSError:
    print("Computer error. Try again.")
try:
    x = (file[0])
except NameError:
    print("you’re just not very good at this, are you?")
try:
    i = int(input("Give me a number: "))
    sol = int(x) - i
    print(sol)
except ValueError:
    print("Close, but no. Try again.")