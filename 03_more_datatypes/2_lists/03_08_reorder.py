'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''

#get numbers from user
inputList = []
nums = input("Give me 10 numbers separated by commas: ")
#print(nums)
#print(inputList)

listt = nums.split(",") #split string by commas
print(listt)
print(nums)

print(type(nums))
print(listt[1])

#
# index = 2
# #while index
# for num in listt:
#     if index < 20:
#         print(listt[index])
#         index += 4
#     # else:
#     #     print(list[index-4])