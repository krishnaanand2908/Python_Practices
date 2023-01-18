# Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".

# My Solution:
def string(str):
    if str[0]== "I" and str[1]=="s":
        return str
    else:
        return "Is"+str

# while 1:
#     string1 = input("Enter your string: ")
#     print(string(string1))

# Sample Solution:
def new_string(str):
  if len(str) >= 2 and str[:2] == "Is":
    return str
  return "Is" + str

print(new_string("Array"))
print(new_string("IsEmpty"))
