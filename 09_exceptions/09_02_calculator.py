'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''

while True:
    try:
        unoInput = int(input("Give me a number: "))
        dosInput = int(input("Give me another number: "))
        print(unoInput / dosInput)
    except ValueError:
        print("I asked for a number, not a string. Try again.")
    except ZeroDivisionError:
        print("Can't divide by zero. Try again with another number.")