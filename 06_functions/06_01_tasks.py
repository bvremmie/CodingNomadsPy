'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results

def or_boolean(n):
        if n % 4 == 0 or n % 7 == 0:
            return True
        else:
            return False


def and_boolean(n):
    if n % 4 == 0 and n % 7 == 0:
        return True
    else:
        return False



input = int(input("Give me a number between 1 and 1,000,000,000: "))
print(f"Input: {input}")

orResult = or_boolean(input)
print(f"{input} is divisible by 4 OR 7: {orResult}")

andResult = and_boolean(input)
print(f"{input} is divisible by 4 AND 7: {andResult}")