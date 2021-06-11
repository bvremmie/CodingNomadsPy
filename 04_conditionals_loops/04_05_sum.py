'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''

#take numbers from user
num1 = int(input("Give me one number between 1 and 100: ")) #store first number
num2 = int(input("Give me one number between 1 and 100: ")) #store second number

nums = range(num1, num2 + 1) # object to call range on inputs

start = 0 # starting point
for n in nums: #loop through range of numbers
    start += n #adds each digit in range to starting point (0)
print(f"The sum is: {start}") #prints sum of range