'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''

string = input("Give me a sentence. ")
string = string.lower()

num_of_vowels = 0
for letter in string:
    if letter == "a":
        num_of_vowels += 1
    elif letter == "e":
        num_of_vowels += 1
    elif letter == "i":
        num_of_vowels += 1
    elif letter == "o":
        num_of_vowels += 1
    elif letter == "u":
        num_of_vowels += 1

print(num_of_vowels)
