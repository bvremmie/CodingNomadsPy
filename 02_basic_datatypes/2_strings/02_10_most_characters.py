'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''

first_input = input("Give me a string. ").lower()
second_input = input("Give me a second string. ").lower()
third_input = input("Give me a third string. ").lower()

print(f"{len(first_input)}, {first_input} \n{len(second_input)}, {second_input} \n{len(third_input)}, {third_input}")

