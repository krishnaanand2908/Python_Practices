# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

# My Solution:
def computer(n):
    n2 = ((str(n))+(str(n)))
    n3 = ((str(n))+(str(n))+(str(n)))
    return ((n) + (int(n2)) + (int(n3)))
n = int(input("Enter n: "))
print(computer(n))

# Sample Solution:
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)
