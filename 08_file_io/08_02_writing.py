'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''


with open("words.txt", "r") as fin:
    words = fin.readlines()



# with open("words_reverse.txt", "w") as fout:
#     fin.writelines():