'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

num = int(input("Give me a number: "))

# months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
#           9: "September", 10: "October", 11: "November", 12: "December"}

months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

"""
if num == months.keys:
    print(months[num])
    """


if num > 12:
    print("Other")
else:
    print(months[num - 1])

# for k in months.keys():
#     if num == k:
#         print(months[k])

# if num > 0 and num < 13:
#     print(months[num])
# else:
#     print("Other")


