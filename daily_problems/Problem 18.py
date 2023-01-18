# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.

# My Solution:
def sum_computer(a, b, c):
    if a == b == c:
        return (a+b+c) * 3
    else:
        return (a+b+c)

print(sum_computer(1, 2, 3))
print(sum_computer(1, 1, 1))

# Sample Solution:
def sum_thrice(x, y, z):

     sum = x + y + z
  
     if x == y == z:
      sum = sum * 3
     return sum

print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))
