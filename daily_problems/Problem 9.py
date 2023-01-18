# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

# My Solution:
exam_st_date = (11, 12, 2014)
# print(type(exam_st_date))
print(f"The exams will start from: {exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}")

# Sample Solution:
exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)
