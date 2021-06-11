'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''
ftemp = int(input("What's the temperature in fahrenheit? "))
ctemp = (ftemp - 32) * (5/9)
ctemp = round(ctemp,2)

print(f"{ftemp} degrees fahrenheit = {ctemp} degrees celsius")
