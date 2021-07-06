'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''


dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4, "d": 2}

# count = {}
# for i in dict_1:
#     c1 = dict_1.count(1)
#     print(c1)


K1 = dict_1.keys()
#print(type(K1))
K1 = list(K1)
#print(type(K1))
K2 = dict_2.keys()
K2 = list(K2)
keys = K1 + K2
#print(keys)

V1 = dict_1.values()
V1 = list(V1)
V2 = dict_2.values()
V2 = list(V2)
vls = V1 + V2
#print(V1, V2)

dict = {}
for k in keys:
    dk1 = 0
    dk2 = 0
    if k in K1:
        dk1 = dict_1[k]
    if k in K2:
        dk2 = dict_2[k]
    dk1 + dk2
    dict[k] = dk1 + dk2
print(dict)

