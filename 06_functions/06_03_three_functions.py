'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''

input = int(input("Give me a number between 1 and 1,000,000,000: "))

def double(n):
    d = n + n
    return d

dblNum = double(input)

def divide(n):
    v = n / 2
    return v

dvNum = divide(dblNum)

def sqr(n):
    sq = n**2
    sqR = round(sq)
    return sqR

sqNum = sqr(dvNum)

print(f"Double input = {dblNum}")
print(f"Half of that is {dvNum}")
print(f"The square of that number is {sqNum}")

