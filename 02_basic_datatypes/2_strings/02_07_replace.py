'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

strinput = input("Give me a sentence. ")
strinput = strinput.lower()
symbol = input("Give me a symbol. ")
newstr = strinput.replace(strinput[0], symbol)
print(newstr)