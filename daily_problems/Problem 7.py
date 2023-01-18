#Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java

# My Solution:
filename = input("Enter the file name: ")
list_of_file_name_and_file_extension = filename.split('.')


if len(list_of_file_name_and_file_extension) >= 2:
    print(f"File extention: {list_of_file_name_and_file_extension[-1]}")
else:
    print("Your file have no extension!")
        
# Sample Solution
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
