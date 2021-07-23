'''
Write a script with a function that demonstrates the use of *args.

'''


def my_function(*yer):
    for lyric in yer:
        print((f"--> {lyric}").upper())


my_function("be", "thankful", "for", "what", "you", "got", "!")
