# Write a Python program that prints the calendar for a given month and year.
# Note : Use 'calendar' module.

# My Solution:
import calendar
year = int(input("Enter the year(as an integer): "))
month = int(input("Enter the month(as an integer): "))
print(calendar.month(year, month))
# print(calendar.calendar(year))

# import calendar
# import fontstyle
# import os
# os.system("cls")
# year = int(input(fontstyle.apply("Enter the year: ", "cyan/bold")))
# print(fontstyle.apply(calendar.calendar(year), "yellow/bold"))

# Sample Solution:
import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))