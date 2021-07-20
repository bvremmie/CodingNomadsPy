'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''

gen = (i for i in range(5556))

for x in gen:
    if x // 1111 == 0 and x != 0:
        print(x)