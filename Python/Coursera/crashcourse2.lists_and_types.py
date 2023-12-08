#from math import *

'''
playing around with math and lists
'''
#lists are built with square brackets, [], can hold any data type
street_names = ['MLK', 'Greene', 'Highland']
fib_numbers = [2, 3, 5, 8, 13, 21]

street_names.append('Electric Ave')
print(street_names)
street_names.sort()
print(street_names)
print('-----------')

#snippet to take an input, and multiple the fib sequence with it
#a_num = input("Please enter a number: ")
#changing to contiue testing without input
a_num = 4
new_list = []
for fibnum in fib_numbers:
    new_list.append(fibnum * a_num)
print(fib_numbers)
print(new_list)
print('-----------')

#tuples are immutable lists, using paranthesis and commas
my_fib_tuple = (1, 2, 3, 5, 8, 13, 21) 
print(my_fib_tuple[5])
print('-----------')

#dictionaries are 'key', 'value' lists, using {}
dict1 = {'color': 'purple', 'size': 'ginormous'}
dict2 = {}  #also dynamic, can be started as empty
print(dict1['color'])
print(dict1['size'])
dict2['speed'] = 'fast'
print(dict2['speed'])
dict2['tuple'] = my_fib_tuple[4]
#reminder: can't print numbers directly, so must turn it into a string
print("my dictionary derived value is " + str(dict2['tuple']))
dict2['toRemove'] = 'REMOVE ME'
print(dict2)
#and to remove
del dict2['toRemove']
print(dict2)

#doing the same with variables?
for dict_key, dict_value in dict1.items():
    dict2[dict_key] = dict_value
print(dict2)
popped = dict2.pop(0, "no key")
print("popped is " + popped + " and dict2 is " + str(dict2.items()))
popped = dict2.pop('size', "no key")
print("trying again, now popped is " + popped + " and dict2 is " + str(dict2.items()))
