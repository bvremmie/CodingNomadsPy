'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def my_function(**yer):
    for i,l in yer.items():
        print(f"this {i} is {l}.")


my_function(artist = "lucky daye", title = "look easy", playtime = 5)
