'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''

nums = input("Write a list of numbers: ")
# nums = int(nums)
# nums = nums.sort()
nums = nums.split(",")

nums.sort()
print(nums)

tupList = []
for i in range(0, len(nums), 2):
    if i+1 < len(nums):
        tupNums = tuple([nums[i], nums[i+1]])
        tupList.append(tupNums)
    else:
        tupNums = tuple([nums[i], 0])
        tupList.append(tupNums)

print(tupList)
