# Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

#My solution:
import datetime
print(f"Current date and time:\n{datetime.datetime.now()}")

# w3resource's solution:
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#Difference is that my output shows the exact seconds and sample solution shows ingores the decimle values