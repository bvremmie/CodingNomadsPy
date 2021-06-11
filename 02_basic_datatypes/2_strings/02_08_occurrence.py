'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

strinput = input("Give me a sentence. ")
strinput = strinput.lower()
letter = input("Give me a letter in the sentence. ")
index = strinput[letter]
print(index)