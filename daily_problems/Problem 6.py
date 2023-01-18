# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

#My solution:
sequence = input("Enter a sequence of numbers separated by a ','\n-->")
list1 = sequence.split(',')
tup1 = tuple(list1)
print(f"List: {list1}\nTuple: {tup1}")

#Sample Solution:
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
