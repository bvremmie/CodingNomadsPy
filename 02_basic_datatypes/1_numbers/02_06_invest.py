'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

inv = int(input("What's the investment amount? "))
intrate = int(input("What's the interest rate in percentage? "))
numyrs = int(input("What's nthe number of years to invest? "))
future = inv*(intrate/100)