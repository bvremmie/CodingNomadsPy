'''
Write a script that takes in a number from the user as input and prints the following structure.

Suppose the input is 5, you will output
*
* *
* * * 
* * * *
* * * * * 
i.e. number of rows will be 5, 1st row will have 1 star, 2nd row will have 2 stars, 3rd row 3 stars, 4th row will have 4 stars and 5th row will have 5 stars.

Another example: if input is 3, you will output
*
* *
* * *

Hint: Think of nested for loops

'''

num = int(input("Give me a number: "))
star = '*'

# n = 0
# while n < num:
#     for n in range(1, num+1):
#         print("*")
#         n += 1


for n in range(1, num+1):
    if n != num+1:
        print(star)
        n += 1
        star += '*'