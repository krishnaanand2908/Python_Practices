# Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference

# My Solution:
n = float(input("Enter your number: "))
if n > 17:
    print(2*(n-17))
else:
    print(17-n)

# Sample Solution:
def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2 

print(difference(22))
print(difference(14))
