three_numbers = (1, 2, 3)
#tuples are immutable
# three_numbers[0] = 4 Output :- 'tuple' object does not support item assignment
print(three_numbers)
print(len(three_numbers))
print(type(three_numbers)) 
#it allows various data types as well a single tuple can have multiple data types 


# as it is an class so we can create tuple using it's constructor

tuple1 = tuple((1, 2, 3))
print(tuple1)